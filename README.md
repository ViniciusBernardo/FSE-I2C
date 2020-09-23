## Versão em Python
Para executar a versão em python, entre com os seguintes comandos no terminal:

```
>> cd python/lcd_16x2_i2c
>> python3 display_measurements.py
```

## Versão em C
Para executar a versão em C, entre com os seguintes comandos no terminal:
```
>> cd c/
>> gcc -o bin create_measurements.c bme280.c
>> ./bin
```

**Limitações da versão C:**
* Os dados no arquivos csv são sobreescritos a cada execução;
* Ao finalizar o programa com ctrl + C, o programa irá concluir ao término do bloco das 10 medições corrente.
