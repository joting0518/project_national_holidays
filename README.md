情境：一個需要注意國定假日是幾號的系統需要存取爬下來的官方資料以利交易執行  
結合sqlalchemy、python flask框架和selenium完成的專案  
先利用爬蟲爬取網路資料並利用flask去呈現狀態，最後結合sqlalchemy將爬取下來的資料存入Database中  

use selenium to go through https://data.gov.tw/dataset/14718, and then read the file which is about government calender.  
And then, process the data and connect to database by sqlalchemy  
SQLAlchemy是一個Python庫，用於簡化與關係型數據庫的交互。它提供了一個抽象層，讓你可以使用Python對數據庫進行操作，而不必直接使用SQL語句。  
do the following steps:  
連接到數據庫->創建一個引擎（Engine）  
定義數據模型->使用SQLAlchemy提供的基礎模型類（declarative base）來定義模型 similar to set titles for the table  
創建表格->創建實際的數據表格  
執行查詢->使用Session來執行查詢和數據操作 新增數據&更新數據&刪除數據  

orm note  
ORM代表對象關係映射（Object-Relational Mapping），它是一種軟件設計模式，用於將關係型數據庫中的數據和面向對象編程語言（如Python、Java、C#等）中的對象建立映射關係，從而實現數據庫和應用程序之間的互操作性。  
在傳統的關係型數據庫中，數據以表格的形式存儲，而在面向對象的編程語言中，數據以對象的形式表示。ORM的目標是將這兩種不同的數據表示方式進行映射，使開發人員能夠使用面向對象的方式來操作數據庫，而不必直接處理SQL語句和數據表格。  
use orm to connect python class and mysql table together  