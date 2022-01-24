from src.domain import commands
from src.adapters import sender


def send_temperature_data(
        cmd: commands.SendTemperatureData,
        sender: sender.AbstractSender,
):
    print('Command: send_temperature_data activated')
    data = {'temperature': cmd.temperature}
    sender.send_async(data)
    return


def send_humidity_data(
        cmd: commands.SendTemperatureData,
        sender: sender.AbstractSender,
):
    print('Command: send_humidity_data activated')
    data = {'humidity': cmd.humidity}
    sender.send_async(data)
    return


def get_number_of_active_threads(
        cmd: commands.SendTemperatureData,
        sender: sender.AbstractSender,
):
    print('Command: get_number_of_active_threads activated')
    return sender.alive_threads_number()


COMMAND_HANDLERS = {
    commands.SendTemperatureData: send_temperature_data,
    commands.SendHumidityData: send_humidity_data,
    commands.GetActiveThreadsNumber: get_number_of_active_threads,
}  # type: Dict[commands.Command, Callable]
