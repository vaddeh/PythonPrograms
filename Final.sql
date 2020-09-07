

  -- Query for How Many rounds are played on average per game?
  select Max(Round_Id) / (select count(distinct Game_Id) from [dbo].[Dice_GameRound]) As AvgNoofGames
  From [dbo].[Dice_GameRound]

  -- Query for long does the average game last? in seconds
  select SUM(datediff(SECOND,[Start_Time],[End_Time])) / (select max([Game_id])  as AvgGameTimeinsec from [dbo].[Dice_Game]) As GameTime from [dbo].[Dice_Game]

  -- Query for Who won more games in a round

  -- Drop Temp1 if Exists by using Drop table ##temp1
  
  select count(Winner) as WinnerCount,Game_Id,winner into  ##temp1
 from  [DiceGame].[dbo].[Dice_GameRound]
 where Winner <> 'draw'
 group by Game_Id,winner

  SELECT distinct a.[Game_Id]
      ,a.[winner]
  FROM [DiceGame].[dbo].[Dice_GameRound] a
  Inner JOIN ##temp1 b
  on a.[Game_Id]=b.[Game_Id]
  AND a.[winner] = b.[winner]
  AND b.WinnerCount = (select Max(WinnerCount) from ##temp1 c where a.Game_id=c.Game_id Group by Game_Id) 

  -- Query for caluculating Roll BreakDown For Each Player
  --Drop table ##temp2
  select * into ##temp2 from (
  Select concat([Human_Die1],concat(',',[Human_Die2])) as Dice,
 'Human' as Player
  from [DiceGame].[dbo].[Dice_GameRound]
  UNION ALL
select concat([Computer_Die1],concat(',',[Computer_Die1])) as Dice,
 'Computer' as Player
  from [DiceGame].[dbo].[Dice_GameRound] 
  ) a


    select dice,(cast(count(dice) as float) /cast((select count(distinct dice) from ##temp2 where Player='Human' ) as float))*100 Percentbreakdown  from ##temp2 where Player='Human' 
  group by Dice

      select dice,(cast(count(dice) as float) /cast((select count(distinct dice) from ##temp2 where Player='Computer' ) as float))*100 Percentbreakdown  from ##temp2 where Player='Computer' 
  group by Dice



  
