from charms.docker.dockeropts import DockerOpts


class TestDockerOpts:

    def test_init(self):
        d = DockerOpts()
        assert isinstance(d.data, dict)

    def test_add(self):
        d = DockerOpts()
        d.add('foo', 'bar')
        assert 'foo' in d.data
        assert d.data['foo'] == ['bar']

    def test_add_multi(self):
        d = DockerOpts()
        d.add('foo', 'bar, baz')
        assert 'foo' in d.data
        assert d.data['foo'] == ['bar', 'baz']

    def test_to_s(self):
        d = DockerOpts()
        d.add('foo', 'bar, baz')
        assert d.to_s() == "--foo=bar --foo=baz"

    def test_remove_single(self):
        d = DockerOpts()
        d.add('foo', 'bar, baz')
        d.remove('foo', 'baz')
        assert 'baz' not in d.data['foo']
        assert 'bar' in d.data['foo']

    def test_data_persistence(self):
        x = DockerOpts()
        x.add('juju', 'is amazing')
        d = DockerOpts()
        assert d.data['juju'] == ['is amazing']

    def test_add_flag_only(self):
        d = DockerOpts()
        d.add('flagonly', None)
        assert(d.data['flagonly'] is None)

    def test_render_flag_only(self):
        d = DockerOpts()
        d.add('flagonly', None)
        assert "--flagonly" in d.to_s()

    def test_strict_options(self):
        d = DockerOpts()
        d.add('strictmode', 'strict-formatting,enabled-because', strict=True)
        assert "--strictmode=strict-formatting,enabled-because" in d.to_s()
