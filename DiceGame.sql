USE [DiceGame]
GO

/****** Object:  Table [dbo].[Dice_Game]    Script Date: 9/5/2020 5:25:15 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Dice_Game](
	[Game_id] [int] IDENTITY(1,1) NOT NULL,
	[Start_Time] [datetime] NULL,
	[End_Time] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[Game_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO


