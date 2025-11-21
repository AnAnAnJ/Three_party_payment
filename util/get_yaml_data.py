import os
import yaml

def test_get_yaml():
    viva_host_url = ""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(current_dir, '..', 'util', 'url_config.yaml')
        with open(config_path, 'r', encoding='utf-8') as f:
            config_data = yaml.safe_load(f)

        # Parse config
        for item in config_data:
            if 'url' in item:
                for url_group in item['url']:
                    if 'Viva' in url_group:
                        for env_config in url_group['Viva']:
                            if 'staging' in env_config:
                                viva_host_url = env_config['staging'][0]
                                print(f"返回的数据{viva_host_url}")
                                return viva_host_url
    except Exception as e:
        print(f"Failed to load config: {e}")

if __name__ == '__main__':
    test_get_yaml()
