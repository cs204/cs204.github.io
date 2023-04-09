<!doctype html>
<html>
	<head>
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> 
	<!-- Bootstrap CSS --> 
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous"> 
	<meta charset="utf-8">
	<link href="style.css" rel="stylesheet">

	<link href="/python23/data/prism/prism.css" rel="stylesheet">

	<title> 
		
    Строки кода.
 
	</title> 
	<link rel="icon" href="data/favicon.ico" type="image/x-icon">
	</head>
	<body>
		<div id=flex>
			<nav>
				<ul>
					<li><a style="font-syze: 3em; font-weight: bold;" href="../index.html">Начало</a></li>
					<li> <a href="discassion.html">Обсуждение</a></li>
					<li><a href="error.html">Замечания</>
					<hr>

					<li><a href="code_cs50_io.html">Неделя 0</a> code.cs50.io</li>
					<li><a href="functions.html">Неделя 1</a> Переменные и фукции</li>
					<li><a href="conditionals.html">Неделя 2</a> Ветвления</li>
					<li><a href="loops.html">Неделя 3</a> Циклы</li>
					<li><a href="exceptions.html">Неделя 4</a> Исключения</li>
					<li><a href="libraries.html">Неделя 5</a> Библиотеки</a></li>
					<li><a href="unitTests.html">Неделя 6</a> Тестирование</a></li>
					<li><a href="file.html">Неделя 7</a> Файловый ввод/вывод.</li>
				
				</ul>
			</nav>
			<main>
				
<h1>Строки коад</h1>
Один из способов оценить сложность программы - посчитать количество
строк кода, исключиая пустые строки и комментарии. Например программа hello.py:
    <pre>
    <code class="language-python">
    #пробный файл для lines.py

    name = input("Waht's you name? ")
    print(f"hello, {name}")
    </code>
    </pre>
  имеет всего две строки кода.
  <p>В файле lines.py реализуйте программу, которая ожиадет один аргумет
  командной строки, имя файла python, возвращает чилсо строк, исключая
  пустые строки и комментарии.
  Если пользователь не указывает точно один аргумент коммандной строки,
  или файл имеет расширение не py, или файла с указанным именем нет, программа
  заканчивает работу через вызов sys.exit.
  </p>
  <p>Предпологаем, что срока комментария начинается с #. Создайте файл hello.py:
<pre>
    <code class="language-python">
    #пробный файл для lines.py

    name = input("Waht's you name? ")
    print(f"hello, {name}")
    </code>
    </pre>
    Он нужен для проверки.
  </p>

<details> 
	<summary>Подсказка</summary> 
	<ul> 
		<li> 
			Тип str имеет много методов, см <a href="https://digitology.tech/docs/python_3/library/stdtypes.html#string-methods">https://digitology.tech/docs/python_3/library/stdtypes.html#string-methods</a>,
            включая lstrip и startwith.
		</li>
		<li> 
        Функция open бросает исключение FileNotFoundError, см <a href="https://digitology.tech/docs/python_3/library/exceptions.html#FileNotFoundError">https://digitology.tech/docs/python_3/library/exceptions.html#FileNotFoundError</a>.
		</li>
	</ul>
</details>

<h2>Демонстрация</h2>
<script async 
    id="asciicast-aiOiXrEwpce7zS4z50u1DnjKV" src="https://asciinema.org/a/aiOiXrEwpce7zS4z50u1DnjKV.js"
	data-autoplay="true" data-loop="true" data-rows="10" data-cols="80">
</script>


<h2>Шаги выполнения</h2>
Зайдите на <a href="https://code.cs50.io">code.cs50.io</a>. 
Используя команду cd, сделайте рабочим каталогом codespace.
Создайте каталог lines,  выполнив
<pre>
<code>mkdir lines</code>
</pre>
Перейдите в каталог.
<pre>
<code>cd lines</code>
</pre>
Выполните 
<pre>
<code>
code lines.py
</code>
</pre>
чтобы открыть редактор, и напишите вашу программу.
Создайте файл hello.py с текстом, приведенным выше.


<h2>Как проверить</h2>
<p>Сделайте рабочим каталог с программой.
</p>
<ul>
	<li>
Запустите программу python lines.py.
Ваша программа должна завершть работу с sys.exit
и вывести сообщение:
<pre>
<code>
Слишком мало аргументов в командной строке
</code>
</pre>
	</li>
	<li>
    Создайте две программы hello.py и
    goodbye.py. Выполните в терминале команду
    python lines.py hello.py goodbye.py.
    Ваша программа должна завершить работу с sys.exit,
    выести сообщение:
<pre>
<code>
Слишком много аргументов в командной строке
</code>
</pre>
	</li>

	<li>
    Создайте файл invalid_extension.txt. Выполните python lines.py invalid_extension.txt. Программа должна завершть через sys.exit,
    вывести:
<pre>
<code>
Не python файл
</code>
</pre>
	</li>
	<li>
Запустите программу python non_existen_file.py.  Прдедпологается, что 
такого файла нет в папке, программа должна обработать исключение и завершить
работу через sys.exit, вывести сообщение:
    <pre>
    <code>
    Файл не существует
    </code>
    </pre>
	</li>
	<li>
    Создайте файл hello.py. Как указано ниже.
    <pre>
    <code class="language-python">
    #пробный файл для lines.py

    name = input("Waht's you name? ")
    print(f"hello, {name}")
    </code>
    </pre>
    Запустите python lines.py hello.py. Программа должна вывести:
        <pre>
        <code>
        2
        </code>
        </pre>
	</li>
</ul>



Вы можете проверить правильность выполнения задания, выполнив команду
<pre>
<code>npx cs204 2023/lines local</code>
</pre>
Для отправки на проверку выполните команду
<pre>
<code>npx cs204 2023/lines</code>
</pre>


<h2>Заполните форму</h2>
<a href="http://90.188.117.161:8080/character/pset/2023/lines/c">форма отправки на проверку</a>
<br>
Свои оценки вы можете посмотреть на <a href="http://90.188.117.161:8080">http://90.188.117.161:8080</a>.
<br>


			</main>
		</div>




		<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous">
		</script> 
		<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous">
		</script> 
		<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous">
		</script>

		<script src="/python23/data/prism/prism.js"></script>
	</body>
</html>