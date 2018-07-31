# Guess Me - PWN, 200 баллов
Загружаем бинарник в IDA. Нажимаем F5 и видим декомпилированный код на C:
```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int v3; // eax@1
  int v4; // eax@1
  FILE *stream; // ST08_8@2
  int result; // eax@4
  __int64 v7; // rsi@4
  char s1; // [sp+10h] [bp-50h]@1    // Сюда загружается строка, введенная пользователем
  char s; // [sp+20h] [bp-40h]@1     // А сюда - сгенерированная при запуске программы
  char ptr; // [sp+30h] [bp-30h]@2
  __int64 v11; // [sp+58h] [bp-8h]@1

  v11 = *MK_FP(__FS__, 40LL);
  v3 = time(0LL);
  srand(v3);
  v4 = rand();
  sprintf(&s, "%d", (unsigned int)(v4 % 10000000 + 1));
  puts("Guess my number [1..10000000] and I will give you a flag");
  fflush(_bss_start);
  __isoc99_scanf("%s", &s1);
  if ( !strcmp(&s1, &s) )
  {
    stream = fopen("flag.txt", "r");
    fread(&ptr, 1uLL, 0x20uLL, stream);
    puts(&ptr);
    fclose(stream);
  }
  else
  {
    puts("Sorry, but you lose :(");
  }
  result = 0;
  v7 = *MK_FP(__FS__, 40LL) ^ v11;
  return result;
}
```
Видим типичный случай уязвимости переполнения буфера. Сделав вводимую строку достаточно длинной, мы можем перезаписать значение числа, сгенерированного компьютером, и таким образом успешно пройти проверку. <br>
Эксплойт можно посмотреть в файле `sploit.py`. <br>
**Флаг:** `uctf_345y_fix3d_pwn`
