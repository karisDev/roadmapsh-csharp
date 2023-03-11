### Основные команды dotnet

| Команда                                                                    | Описание                                  |
| -------------------------------------------------------------------------- | ----------------------------------------- |
| donnet new --list                                                          | все возможные проекты для создания        |
| dotnet new gitignore                                                       | создать крутой гитигнор                   |
| dotnet new console DemoApp                                                 | создать папку DemoApp с проектом внутри   |
| dotnet new sln                                                             | создать решение                           |
| dotnet sln add DemoApp                                                     | добавить к решению проект                 |
| dotnet new classlib -o DemoLib                                             | создать класс в папке DemoLib             |
| dotnet add package Dapper                                                  | добавить NuGet пакет в проект             |
| dotnet add reference ..\DemoLib\DemoLib.csproj                             | Добавить референс из DemoApp в DemoLib    |
| dotnet restore                                                             | npm i по сути                             |
| dotnet build                                                               | собрать проект, создается папка bin/Debug |
| dotnet clean                                                               | убрать из билда лишние файлы              |
| dotnet rebuild                                                             | clean + build                             |
| dotnet run                                                                 | запуск проекта в текущей папке            |
| dotnet publish -p:PublishSingleFile=true -r win-x64 --self-contained false | билд в виде одного exe и без .Net Core    |

### Полезные ссылки

[Runtime Identifiers](https://learn.microsoft.com/en-us/dotnet/core/rid-catalog)
