from jina import Flow
from jina.importer import ImportExtensions
from jina.logging.predefined import default_logger
from jina.logging.profile import ProgressBar
from jina.parsers.helloworld import set_hw_chatbot_parser
from jina.types.document.generators import from_csv



workspace_dir = os.path.join(os.path.abspath('workspace'))

if __name__ == '__main__':
    from flow.executers import MyTransformer, MyIndexer
else:
    from executers import MyTransformer, MyIndexer


def _get_flow():
    """Ensure the same flow is used in hello world example and system test."""
    return (
        Flow(cors=True)
        .add(uses=MyTransformer)
        .add(uses=MyIndexer, workspace=workspace_dir)
    )


def activate():
    

    f = _get_flow()

    # index it!
    with f, open('data.csv') as fp:
        f.index(from_csv(fp, field_resolver={'question': 'text'}), show_progress=True)
      
        f.block()

activate()