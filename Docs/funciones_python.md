# 🐍 Funciones integradas de Python

Referencia rápida de las funciones *built-in* de Python (3.13). Estas funciones están disponibles siempre, sin necesidad de usar `import`.

## 📑 Índice

- [🐍 Funciones integradas de Python](#-funciones-integradas-de-python)
  - [📑 Índice](#-índice)
  - [📥 Entrada y salida](#-entrada-y-salida)
  - [🔄 Conversión de tipos y constructores](#-conversión-de-tipos-y-constructores)
  - [➗ Matemáticas](#-matemáticas)
  - [🔢 Representación y conversión de números y texto](#-representación-y-conversión-de-números-y-texto)
  - [🔁 Iteración y secuencias](#-iteración-y-secuencias)
  - [⚡ Programación asíncrona](#-programación-asíncrona)
  - [🧱 Objetos, clases y atributos](#-objetos-clases-y-atributos)
  - [🔍 Introspección y entorno](#-introspección-y-entorno)
  - [🚀 Ejecución dinámica](#-ejecución-dinámica)

---

## 📥 Entrada y salida

| Función   | Descripción                               |
| --------- | ----------------------------------------- |
| `print()` | Muestra valores en pantalla.              |
| `input()` | Lee texto escrito por el usuario.         |
| `open()`  | Abre un archivo para leerlo o escribirlo. |
| `help()`  | Muestra la ayuda de un objeto o función.  |

## 🔄 Conversión de tipos y constructores

| Función        | Descripción                                       |
| -------------- | ------------------------------------------------- |
| `int()`        | Convierte a número entero.                        |
| `float()`      | Convierte a número decimal.                       |
| `complex()`    | Crea un número complejo.                          |
| `str()`        | Convierte a cadena de texto.                      |
| `bool()`       | Convierte a booleano (`True` / `False`).          |
| `list()`       | Crea una lista.                                   |
| `tuple()`      | Crea una tupla.                                   |
| `set()`        | Crea un conjunto.                                 |
| `frozenset()`  | Crea un conjunto inmutable.                       |
| `dict()`       | Crea un diccionario.                              |
| `bytes()`      | Crea una secuencia inmutable de bytes.            |
| `bytearray()`  | Crea una secuencia mutable de bytes.              |
| `memoryview()` | Da acceso a la memoria de un objeto sin copiarlo. |
| `object()`     | Crea un objeto base vacío.                        |
| `slice()`      | Crea un objeto de rebanado (`[a:b:c]`).           |
| `range()`      | Genera una secuencia de números.                  |

## ➗ Matemáticas

| Función    | Descripción                                |
| ---------- | ------------------------------------------ |
| `abs()`    | Valor absoluto.                            |
| `round()`  | Redondea un número.                        |
| `pow()`    | Potencia (`x ** y`), con módulo opcional.  |
| `divmod()` | Devuelve cociente y resto de una división. |
| `sum()`    | Suma los elementos de un iterable.         |
| `min()`    | Devuelve el valor mínimo.                  |
| `max()`    | Devuelve el valor máximo.                  |

## 🔢 Representación y conversión de números y texto

| Función    | Descripción                                               |
| ---------- | --------------------------------------------------------- |
| `bin()`    | Entero a binario (texto).                                 |
| `oct()`    | Entero a octal.                                           |
| `hex()`    | Entero a hexadecimal.                                     |
| `chr()`    | Código Unicode a carácter.                                |
| `ord()`    | Carácter a código Unicode.                                |
| `ascii()`  | Representación del objeto usando solo caracteres ASCII.   |
| `repr()`   | Representación "oficial" de un objeto, útil para depurar. |
| `format()` | Da formato a un valor según una especificación.           |

## 🔁 Iteración y secuencias

| Función       | Descripción                                   |
| ------------- | --------------------------------------------- |
| `len()`       | Cantidad de elementos de un objeto.           |
| `enumerate()` | Devuelve pares (índice, elemento).            |
| `zip()`       | Combina varios iterables elemento a elemento. |
| `map()`       | Aplica una función a cada elemento.           |
| `filter()`    | Filtra elementos según una condición.         |
| `sorted()`    | Devuelve una lista ordenada.                  |
| `reversed()`  | Devuelve un iterador invertido.               |
| `iter()`      | Crea un iterador a partir de un iterable.     |
| `next()`      | Obtiene el siguiente elemento de un iterador. |
| `all()`       | `True` si todos los elementos son verdaderos. |
| `any()`       | `True` si al menos uno es verdadero.          |

## ⚡ Programación asíncrona

| Función   | Descripción                                             |
| --------- | ------------------------------------------------------- |
| `aiter()` | Obtiene un iterador asíncrono.                          |
| `anext()` | Obtiene el siguiente elemento de un iterador asíncrono. |

## 🧱 Objetos, clases y atributos

| Función          | Descripción                                                |
| ---------------- | ---------------------------------------------------------- |
| `type()`         | Devuelve el tipo de un objeto, o crea una clase nueva.     |
| `isinstance()`   | Comprueba si un objeto es instancia de una clase.          |
| `issubclass()`   | Comprueba si una clase hereda de otra.                     |
| `super()`        | Accede a la clase padre.                                   |
| `getattr()`      | Obtiene el valor de un atributo por su nombre.             |
| `setattr()`      | Asigna un atributo por su nombre.                          |
| `hasattr()`      | Comprueba si existe un atributo.                           |
| `delattr()`      | Elimina un atributo.                                       |
| `callable()`     | Comprueba si un objeto se puede llamar como función.       |
| `property()`     | Define atributos con *getter* / *setter*.                  |
| `classmethod()`  | Marca un método que recibe la clase (`cls`).               |
| `staticmethod()` | Marca un método que no recibe ni la clase ni la instancia. |

## 🔍 Introspección y entorno

| Función     | Descripción                                                     |
| ----------- | --------------------------------------------------------------- |
| `dir()`     | Lista los nombres y atributos de un objeto o del ámbito actual. |
| `vars()`    | Devuelve el `__dict__` de un objeto.                            |
| `globals()` | Diccionario de variables globales.                              |
| `locals()`  | Diccionario de variables locales.                               |
| `id()`      | Identificador único (dirección) de un objeto.                   |
| `hash()`    | Valor hash de un objeto.                                        |

## 🚀 Ejecución dinámica

| Función        | Descripción                                                      |
| -------------- | ---------------------------------------------------------------- |
| `eval()`       | Evalúa una expresión escrita como texto.                         |
| `exec()`       | Ejecuta código Python escrito como texto.                        |
| `compile()`    | Compila código fuente a un objeto ejecutable.                    |
| `__import__()` | Función interna que usa `import` (rara vez se usa directamente). |
| `breakpoint()` | Abre el depurador en ese punto del código.                       |

---

> **Nota:** esta lista solo cubre las funciones integradas. No incluye los **métodos** de los tipos (como `str.split()` o `list.append()`) ni las funciones de **módulos** (como `math.sqrt()` u `os.listdir()`).

📚 Documentación oficial: [docs.python.org/es/3/library/functions.html](https://docs.python.org/es/3/library/functions.html)