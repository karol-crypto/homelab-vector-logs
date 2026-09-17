To install Vector we can use instruction of official website

    https://vector.dev/docs/setup/installation/

Next step is configuration _vector.yaml_ file and start vector.

To chceck our configuration we can use this command:

    vector validate --config /etc/vector/vector.toml

Next:

    sudo systemctl start vector

or if we want to update configuration:

    sudo systemctl restart vector

To check status:

    sudo systemctl status vector


If we want Vector to launch when computer starts, we can use this command:

    sudo systemctl enable vector
