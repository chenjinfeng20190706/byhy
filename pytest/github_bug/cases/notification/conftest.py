import pytest 

@pytest.fixture(scope='package',autouse=True)
def st_notification():
    print(f'\n==== setup：：notification')
    yield
    
    print(f'\n==== teardown：：notification')