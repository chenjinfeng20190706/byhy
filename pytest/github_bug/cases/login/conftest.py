import pytest 

@pytest.fixture(scope='package',autouse=True)
def st_login():
    print(f'\n==== setup：：login')
    yield
    
    print(f'\n==== teardown：：login')