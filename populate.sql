use test;
DROP TABLE IF EXISTS `Books`;
DROP TABLE IF EXISTS `Authors`;
CREATE Table `Authors`
(
   `AId` int,
   `Author_name` nvarchar(50),
   `country` nvarchar(50),
   PRIMARY KEY(`AId`)
)ENGINE = InnoDB DEFAULT CHARSET = latin1;

CREATE Table `Books`
(
   `BId` int ,
   `AId` int ,
   `Price` int,
   `Edition` int,
   CONSTRAINT `Books_ibfk_1` FOREIGN KEY(`AId`) REFERENCES `Authors`(`AId`),
   PRIMARY KEY(`BId`)
)ENGINE = InnoDB DEFAULT CHARSET = latin1;

Declare Id int;
Set Id = 1;

While Id <= 12000;
Begin 
   Insert Into Authors values ('Author - ' + CAST(Id as nvarchar(10)),
              'Country - ' + CAST(Id as nvarchar(10)) + ' name');
   Print Id;
   Set Id = Id + 1
End;