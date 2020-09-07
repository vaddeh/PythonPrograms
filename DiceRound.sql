USE [DiceGame]
GO

/****** Object:  Table [dbo].[Dice_GameRound]    Script Date: 9/5/2020 5:25:40 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Dice_GameRound](
	[Round_Id] [int] IDENTITY(1,1) NOT NULL,
	[Game_Id] [int] NULL,
	[Human_Die1] [int] NULL,
	[Human_Die2] [int] NULL,
	[Computer_Die1] [int] NULL,
	[Computer_Die2] [int] NULL,
	[winner] [varchar](20) NULL,
PRIMARY KEY CLUSTERED 
(
	[Round_Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Dice_GameRound]  WITH CHECK ADD FOREIGN KEY([Game_Id])
REFERENCES [dbo].[Dice_Game] ([Game_id])
GO


