from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, ConversationHandler, ContextTypes, filters, ApplicationBuilder
import os
import base64

#FLAG: URJC{M1r4_como_muEv3_Lo5_0j1t0s}
#37g/Dn$# XOR URJC-CTF = fe-li-pe
# Token del bot
BOT_TOKEN = "8134898285:AAHHkBIWmAolED-PHNC4CSt0uQzYp2F3hwo"

# Diccionario para rastrear si un usuario está en JTD_Mode
user_states = {}

# Función para entrar en JTD_Mode
async def jtd_mode(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    output = base64.b64encode(b'Bienvenido a JTD_Mode. Ahora puedes usar los comandos \n/znati, \n/rk00, \n/drey, y \n/granusti. \n/exit para salir del JTD_Mode.').decode('utf-8')
    user_states[user_id] = True  # Cambiar el estado del usuario a JTD_Mode
    await update.message.reply_text(output)

# Función para salir de JTD_Mode
async def exit_jtd_mode(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if user_states.get(user_id):  # Verificar si el usuario estaba en JTD_Mode
        user_states[user_id] = False
        await update.message.reply_text("Has salido de JTD_Mode.")
    else:
        await update.message.reply_text("No estás en JTD_Mode.")

# Funciones para los comandos dentro de JTD_Mode
async def drey(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if user_states.get(update.effective_user.id):
        mensaje = b'Yo te voy a dar la llave necesaria para resolver el misterio del tiktok:\n"URJC-CTF!"'
        mensaje_codificado = base64.b64encode(mensaje).decode('utf-8')
        await update.message.reply_text(mensaje_codificado)
    else:
        await update.message.reply_text("Debes estar en JTD_Mode para usar este comando.")

async def rk00(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if user_states.get(update.effective_user.id):
        mensaje = b'Te voy a dar una parte del misterio del tiktok:\n"37g/Dn$#"'
        mensaje_codificado = base64.b64encode(mensaje).decode('utf-8')
        await update.message.reply_text(mensaje_codificado)
    else:
        await update.message.reply_text("Debes estar en JTD_Mode para usar este comando.")


async def granusti(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if user_states.get(user_id):
        # Mensaje de texto codificado en Base64
        mensaje = b'Este fichero no es lo que parece, creo que nos estamos pasando con el base64'
        mensaje_codificado = base64.b64encode(mensaje).decode('utf-8')
        await update.message.reply_text(mensaje_codificado)

        # Ruta del archivo 'secreto.txt' en el mismo directorio que el script
        file_path = os.path.join(os.path.dirname(__file__), 'secreto.txt')
        if os.path.exists(file_path):
            # Enviar el archivo al usuario
            await update.message.reply_document(document=open(file_path, 'rb'))
        else:
            await update.message.reply_text("El archivo 'secreto.txt' no se encuentra en el directorio.")
    else:
        await update.message.reply_text("Debes estar en JTD_Mode para usar este comando.")


# Estados de la conversación
WAITING_FOR_INPUT = range(1)

async def znati(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.effective_user.id
    if user_states.get(user_id):
        mensaje = b'Hace poco vi un tiktok que me hizo mucha gracia, pero ahora no se como encontrarlo, drey, rk00 y granusti lo saben pero no me lo quieren decir. \nSi me ayudas te recompensare con lo que mas deseas!'
        mensaje_codificado = base64.b64encode(mensaje).decode('utf-8')
        await update.message.reply_text(mensaje_codificado)
        # Pasar al estado de esperar el input
        return WAITING_FOR_INPUT
    else:
        await update.message.reply_text("Debes estar en JTD_Mode para usar este comando.")
        return ConversationHandler.END


async def check_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_id = update.effective_user.id
    user_input = update.message.text

    if user_input == "fe-li-pe":
        respuesta = (
            "LO ENCONTRE!! muchas gracias toma tu flag URJC{M1r4_como_muEv3_Lo5_0j1t0s}\n "
            "https://www.tiktok.com/@viralysinquehacer/video/7442934816141577527"
        )
        await update.message.reply_text(respuesta)
        # Finalizar la conversación
        return ConversationHandler.END
    else:
        # Si el input es incorrecto, sacar al usuario de JTD_Mode
        user_states[user_id] = False
        await update.message.reply_text(
            "Ese no es el texto correcto. ¡Fallaste y ahora has salido de JTD_Mode!"
        )
        return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("¡Operación cancelada!")
    return ConversationHandler.END

async def handle_unexpected(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Manejar cualquier otro comando o mensaje inesperado durante la espera de input."""
    await update.message.reply_text("Se ha detectado un error, vuelve a ejecutar /znati e introduce el input.")
    return ConversationHandler.END

# Configuración del ConversationHandler para znati
znati_handler = ConversationHandler(
    entry_points=[CommandHandler("znati", znati)],
    states={
        WAITING_FOR_INPUT: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, check_input),
            MessageHandler(filters.COMMAND, handle_unexpected),  # Captura otros comandos
        ],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)

# Función para manejar el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("¡Hola! Vamos a ver si eres capaz de quitarle la flag al bot. Usa /help para ver los comandos que puedes usar")

# Función para manejar el comando /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Aquí está la lista de comandos disponibles:\n/start - Iniciar el bot\n/help - Mostrar ayuda\n/flag - Dar la flag\n/jtd_mode - ????")

# Función fake Flag
async def flag(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("bm8gaWJhIGEgc2VyIHRhbiBmYWNpbA==")

# Configuración principal del bot
def main() -> None:
    # Crear la aplicación del bot con el token
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Añadir manejadores para los comandos principales
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("flag", flag))
    application.add_handler(CommandHandler("jtd_mode", jtd_mode))
    application.add_handler(CommandHandler("exit", exit_jtd_mode))

    # Añadir manejadores para los comandos de JTD_Mode
    application.add_handler(CommandHandler("drey", drey))
    application.add_handler(CommandHandler("rk00", rk00))
    application.add_handler(CommandHandler("granusti", granusti))

    # Agregar el ConversationHandler para znati
    application.add_handler(znati_handler)

    # Iniciar el bot
    application.run_polling()

if __name__ == "__main__":
    main()