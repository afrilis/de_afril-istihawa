OOP (Object Oriented Programming)
Pemrograman berorientasi objek adalah paradigma yang memungkinkan kita mengorganisir program sehingga perilaku dan properti di kelola oleh individu. 
Properti ditentukan oleh nilai atribut, sedangkan perilaku akan ditentukan dari bagaimana objek tersebut bertindak atau reaksi terhadap permintaan. 

Fundamental konsep OOP
1. Encapsulation. Merupakan seni dari pembungkusan objek. Melibatkan pengelompokan atribut dan metode dalam satu unit yang dikenal dengan kelas.
Basic encapsularion analogy: 
- class (template/blueprint) berisikan beberapa atribut atau metode,
- attributes, 
- method.

2. Data Abstraction. Adalah konsep dimana kita hanya menampilkan fitur-fitur penting dari suatu objek dan menyembunyikan detail kompleksnya. 

3. Inheritance. Seni pewarisan objek. Memungkinkan kita untuk merevisi kode dari kelas lain, sehingga tidak perlu menuliskan kode yang sama. Inheritance sebagai cara untuk mengambil apa yang sudah ada dan menambahkan atau mengubah beberapa bagian untuk membuat beberapa yang baru.
Kata kunci Super sering digunakan untuk memanggil metode dari kelas induk, memungkinkan untuk menggunakan metode yang sudah ada dan menambahkan logika tambahan yang diperlukan. 
Selain itu ada Method Overriding (menggunakan dari kelas induk namun di modifikasi sesaui kebutuhan)

4. Polymorphism. Salah satu bagian ajaib dari inheritance/pewarisan. Polymorphism = kemampuan objek dari tipe yang berbeda, untuk merespon fungsi dengan nama yang sama. Sehingga memungkinkan untuk mendefinisikan satu antar muka yang digunakan oleh berbagai jenis objek. 
Contoh : method speak dengan objek cat, duck, dog
class animal - metode speak - class turunan cat, duck, dog. Maka outputnya speak untuk berbagai objeknya sesuai. 