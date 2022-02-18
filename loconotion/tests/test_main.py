import modules.main as main

def test_single_page_arg():
    arg_parser = main.get_arg_parser()

    args = arg_parser.parse_args("target".split())
    print(args)
    assert args.single_page is None

    args = arg_parser.parse_args("target --single-page".split())
    print(args)
    assert args.single_page == ""

    args = arg_parser.parse_args("target --single-page a-page-URL".split())
    print(args)
    assert args.single_page == "a-page-URL"
