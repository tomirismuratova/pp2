"""
Git — это программа с текстовым интерфейсом, с которой надо работать в командной строке. 

Репозиторий
Репозиторий Git — это хранилище, в котором расположен ваш проект и его история. 
Репозиторий служит для отслеживания изменений в проекте, координации работы между несколькими людьми и отслеживания истории проекта.

Репозиторий - это хранилище проекта + истории изменений.
Бывает:
локальный (на твоём ПК);
удалённый (GitHub, GitLab, Bitbucket).
При инициализации (git init) создаётся скрытая папка .git, где Git хранит все данные (историю, настройки, ссылки на ветки).

Коммит
Это снимок изменений в проекте.
Коммит содержит только информацию об изменениях, которые были внесены в репозиторий с момента последнего коммита. 
Он не содержит все файлы репозитория (если только это не первый коммит). Коммиты образуют цепочку истории репозитория, основанный на предыдущем коммите. 

Ветка
Ветка — это параллельная версия репозитория. 
Ветки позволяют вам работать над отдельными функциями вашего проекта, не влияя на основную версию. 
Закончив работу над новой фичей, вы можете объединить эту ветку с основной версией проекта.

Эти данные используются для подписи изменений сделанных вами, что позволит отслеживать, кто и когда сделал изменения в файле.
git config --global user.name "Your Name"
git config --global user.email "your_email@whatever.com"

 main в качестве имени ветки по умолчанию.
git config --global init.defaultBranch main

git config --global core.autocrlf input
git config --global core.safecrlf warn


mkdir work
cd work
touch hello.html
Чтобы создать Git-репозиторий из этой директории, выполните команду git init.
git init

git add hello.html
git commit -m "Initial Commit"

Используйте команду git status, чтобы проверить текущее состояние репозитория.
git status

 просматривать историю проекта.
git log
Однострочная история
git log --pretty=oneline

--pretty="..." — определяет формат вывода.
%ad — дата коммита.
| — просто визуальный разделитель.
%s — комментарий.
%d — дополнения коммита («головы» веток или теги).
%an — имя автора.
--date=short — сохраняет формат даты коротким и симпатичным.
git log --pretty=format:"%h %ad | %s%d [%an]" --date=short

git status → Shows what changed in your project.

git add → Selects the files you want to save. (you can write "git add ." to add all changes/added files, so u can not write git add to each file separately)

git commit → Saves the selected files with a message. git commit -m "message"

git push → Sends your saved changes to GitHub

"""