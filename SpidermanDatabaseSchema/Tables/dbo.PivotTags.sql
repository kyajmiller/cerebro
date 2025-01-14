CREATE TABLE [dbo].[PivotTags]
(
[PivotTagId] [int] NOT NULL IDENTITY(1, 1),
[Predicted] [nvarchar] (500) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Tag] [nvarchar] (500) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[PivotLeadId] [int] NOT NULL,
[Keyword] [nvarchar] (200) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
[Url] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Name] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Abstract] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Sponsor] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Amount] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[ApplicantType] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[CitizenshipResidency] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[ActivityLocation] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Eligibility] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[Categories] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[SourceWebsite] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[SourceText] [nvarchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[PivotTags] ADD CONSTRAINT [PK_PivotTags] PRIMARY KEY CLUSTERED  ([PivotTagId]) ON [PRIMARY]
GO
