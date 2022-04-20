print("""
Module(
    body=[
        Expr(
            value=Call(
                func=Name(id='exec', ctx=Load()),
                args=[
                    Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='path',
                                ctx=Load()),
                            attr='join',
                            ctx=Load()),
                        args=[
                            Name(id='local_dir', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='urllib', ctx=Load()),
                                                attr='parse',
                                                ctx=Load()),
                                            attr='quote',
                                            ctx=Load()),
                        keywords=[])],
                keywords=[]))],
    type_ignores=[])
""")
print("""
Module(
    body=[
        FunctionDef(
            name='theInput',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='var1'),
                    arg(arg='var2')],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[]),
            body=[
                Assign(
                    targets=[
                        Name(id='var_one', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='urllib', ctx=Load()),
                                attr='parse',
                                ctx=Load()),
                            attr='quote',
                            ctx=Load()),
                        args=[
                            Name(id='var1', ctx=Load())],
                        keywords=[])),
                Assign(
                    targets=[
                        Name(id='final_command_two', ctx=Store())],
                    value=JoinedStr(
                        values=[
                            Constant(value='otherprogram /hard/coded/path2/'),
                            FormattedValue(
                                value=Name(id='var_two', ctx=Load()),
                                conversion=-1)])),
                    orelse=[],
                    finalbody=[]),
                Return(
                    value=Constant(value='someOutput'))],
            decorator_list=[])],
    type_ignores=[])
""")

print("The Time taken for Traditional Monte Carlo is 8.134ms")