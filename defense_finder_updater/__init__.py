from macsypy.scripts.macsydata import main as mdmain


def update_models(models_dir, force_reinstall: bool):
    # Updating DefenseFinder models
    cmd_args = ['install', '-U']
    if models_dir is not None:
        cmd_args.extend(['-t', models_dir])
    else:
        cmd_args.append('-u')
    if force_reinstall:
        cmd_args.append('-f')
    cmd_args.extend(['--org', 'mdmparis', 'defense-finder-models'])
    mdmain(cmd_args)

    # Updating CASFinder models
    cmd_args = ['install', '-U']
    if models_dir is not None:
        cmd_args.extend(['-t', models_dir])
    else:
        cmd_args.append('-u')
    if force_reinstall:
        cmd_args.append('-f')
    cmd_args.append('CasFinder')
    mdmain(cmd_args)

