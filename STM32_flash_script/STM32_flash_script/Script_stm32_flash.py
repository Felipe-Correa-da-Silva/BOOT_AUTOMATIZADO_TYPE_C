import subprocess

# O arquivo executável para cada sistema operacional
exe_windows = 'stm32flash.exe'
exe_macOS   = 'stm32flash_linux'
exe_linux   = 'stm32flash_macos'

def boot_update(exec, caminho_bin_hex, porta):
    algoritmo_boot = ' -i ,,,-dtr,,,rts,,,-rts,,,dtr,,, '
    algoritmo_update = ' -w ' + caminho_bin_hex + ' -v -g 0x0 '
    
    # Comando para entrar em modo BOOT
    comando = exec + algoritmo_boot + porta
    subprocess.call(comando, shell=True)
    
    # Comando para enviar o arquivo binário para o STM32 e sair do modo BOOT
    comando = exec + algoritmo_update + porta
    subprocess.call(comando, shell=True)


boot_update(exe_windows, 'test_uart2.bin', 'COM8')