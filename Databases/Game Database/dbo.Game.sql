CREATE TABLE [dbo].[Games](
    [Id]          INT            IDENTITY (1, 1) NOT NULL,
    [Title]       NVARCHAR (MAX) NOT NULL,
    [ReleaseYear] NVARCHAR (4)   NULL,
    [Rating]      INT            NOT NULL,
    [Developer]   NVARCHAR (MAX) NULL,
    [Genre]       NVARCHAR (MAX) NULL,
    [Publisher]   NVARCHAR (MAX) NULL,
    CONSTRAINT [PK_Games] PRIMARY KEY CLUSTERED ([Id] ASC)
);

