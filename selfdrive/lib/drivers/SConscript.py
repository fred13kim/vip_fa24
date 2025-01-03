# ruff: noqa: F821

Import('env')

env.AppendUnique(
    CPPPATH=[
        env.Dir(f'{dir}')
        for dir in [
            'mpu6050',
            'hal',
        ]
    ]
)

drivers = env.SConscript(
    [
        f'{driver}/SConscript.py'
        for driver in [
            'mpu6050',
            'hal',
        ]
    ]
)

Return('drivers')
