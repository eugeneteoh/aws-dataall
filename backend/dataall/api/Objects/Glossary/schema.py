from ... import gql
from .resolvers import *


GlossaryNode = gql.Union(
    name='GlossaryNode',
    types=[
        gql.Ref('Glossary'),
        gql.Ref('Category'),
        gql.Ref('Term'),
    ],
    resolver=resolve_glossary_node,
)

GlossaryChildrenSearchResult = gql.ObjectType(
    name='GlossaryChildrenSearchResult',
    fields=[
        gql.Field(name='count', type=gql.Integer),
        gql.Field(name='page', type=gql.Integer),
        gql.Field(name='pages', type=gql.Integer),
        gql.Field(name='hasNext', type=gql.Boolean),
        gql.Field(name='hasPrevious', type=gql.Boolean),
        gql.Field(name='nodes', type=gql.ArrayType(gql.Ref('GlossaryNode'))),
    ],
)

Glossary = gql.ObjectType(
    name='Glossary',
    fields=[
        gql.Field(name='nodeUri', type=gql.ID),
        gql.Field(name='parentUri', type=gql.NonNullableType(gql.String)),
        gql.Field(name='status', type=gql.String),
        gql.Field(name='owner', type=gql.NonNullableType(gql.String)),
        gql.Field(name='path', type=gql.NonNullableType(gql.String)),
        gql.Field(name='label', type=gql.NonNullableType(gql.String)),
        gql.Field(name='name', type=gql.NonNullableType(gql.String)),
        gql.Field(name='admin', type=gql.String),
        gql.Field(name='readme', type=gql.String),
        gql.Field(name='created', type=gql.NonNullableType(gql.String)),
        gql.Field(name='updated', type=gql.String),
        gql.Field(name='deleted', type=gql.String),
        gql.Field(name='isMatch', type=gql.Boolean),
        gql.Field(
            name='assetLink',
            args=[gql.Argument(name='targetUri', type=gql.NonNullableType(gql.String))],
            resolver=resolve_link,
            type=gql.Ref('GlossaryTermLink'),
        ),
        gql.Field(
            name='stats', resolver=resolve_stats, type=gql.Ref('GlossaryNodeStatistics')
        ),
        gql.Field(
            resolver=node_tree,
            args=[
                gql.Argument(name='filter', type=gql.Ref('GlossaryNodeSearchFilter'))
            ],
            name='tree',
            type=gql.Ref('GlossaryChildrenSearchResult'),
        ),
        gql.Field(
            resolver=list_node_children,
            args=[
                gql.Argument(name='filter', type=gql.Ref('GlossaryNodeSearchFilter'))
            ],
            name='children',
            type=gql.Ref('GlossaryChildrenSearchResult'),
        ),
        gql.Field(
            name='categories',
            args=[gql.Argument(name='filter', type=gql.Ref('CategoryFilter'))],
            resolver=resolve_categories,
            type=gql.Ref('CategorySearchResult'),
        ),
        gql.Field(
            name='associations',
            args=[
                gql.Argument(name='filter', type=gql.Ref('GlossaryTermTargetFilter'))
            ],
            resolver=resolve_term_associations,
            type=gql.Ref('TermLinkSearchResults'),
        ),
    ],
)


Category = gql.ObjectType(
    name='Category',
    fields=[
        gql.Field(name='nodeUri', type=gql.ID),
        gql.Field(name='parentUri', type=gql.NonNullableType(gql.String)),
        gql.Field(name='owner', type=gql.NonNullableType(gql.String)),
        gql.Field(name='path', type=gql.NonNullableType(gql.String)),
        gql.Field(name='label', type=gql.NonNullableType(gql.String)),
        gql.Field(name='status', type=gql.NonNullableType(gql.String)),
        gql.Field(name='name', type=gql.NonNullableType(gql.String)),
        gql.Field(name='readme', type=gql.String),
        gql.Field(name='created', type=gql.NonNullableType(gql.String)),
        gql.Field(name='updated', type=gql.String),
        gql.Field(name='deleted', type=gql.String),
        gql.Field(name='isMatch', type=gql.Boolean),
        gql.Field(
            name='assetLink',
            args=[gql.Argument(name='targetUri', type=gql.NonNullableType(gql.String))],
            resolver=resolve_link,
            type=gql.Ref('GlossaryTermLink'),
        ),
        gql.Field(
            name='stats', resolver=resolve_stats, type=gql.Ref('GlossaryNodeStatistics')
        ),
        gql.Field(
            resolver=list_node_children,
            args=[
                gql.Argument(name='filter', type=gql.Ref('GlossaryNodeSearchFilter'))
            ],
            name='children',
            type=gql.Ref('GlossaryChildrenSearchResult'),
        ),
        gql.Field(
            name='categories',
            resolver=resolve_categories,
            args=[
                gql.Argument(name='filter', type=gql.Ref('CategoryFilter')),
            ],
            type=gql.Ref('CategorySearchResult'),
        ),
        gql.Field(
            name='terms',
            resolver=resolve_terms,
            args=[
                gql.Argument(name='filter', type=gql.Ref('TermFilter')),
            ],
            type=gql.Ref('TermSearchResult'),
        ),
        gql.Field(
            name='associations',
            args=[
                gql.Argument(name='filter', type=gql.Ref('GlossaryTermTargetFilter'))
            ],
            resolver=resolve_term_associations,
            type=gql.Ref('TermLinkSearchResults'),
        ),
    ],
)

Term = gql.ObjectType(
    name='Term',
    fields=[
        gql.Field(name='nodeUri', type=gql.ID),
        gql.Field(name='parentUri', type=gql.NonNullableType(gql.String)),
        gql.Field(name='owner', type=gql.NonNullableType(gql.String)),
        gql.Field(name='path', type=gql.NonNullableType(gql.String)),
        gql.Field(name='label', type=gql.NonNullableType(gql.String)),
        gql.Field(name='name', type=gql.NonNullableType(gql.String)),
        gql.Field(name='status', type=gql.NonNullableType(gql.String)),
        gql.Field(name='readme', type=gql.String),
        gql.Field(name='created', type=gql.NonNullableType(gql.String)),
        gql.Field(name='updated', type=gql.String),
        gql.Field(name='deleted', type=gql.String),
        gql.Field(name='isMatch', type=gql.Boolean),
        gql.Field(
            name='assetLink',
            args=[gql.Argument(name='targetUri', type=gql.NonNullableType(gql.String))],
            resolver=resolve_link,
            type=gql.Ref('GlossaryTermLink'),
        ),
        gql.Field(
            resolver=list_node_children,
            args=[
                gql.Argument(name='filter', type=gql.Ref('GlossaryNodeSearchFilter'))
            ],
            name='children',
            type=gql.Ref('GlossaryChildrenSearchResult'),
        ),
        gql.Field(
            name='stats', resolver=resolve_stats, type=gql.Ref('GlossaryNodeStatistics')
        ),
        gql.Field(
            name='glossary', type=gql.Ref('Glossary'), resolver=resolve_term_glossary
        ),
        gql.Field(
            name='associations',
            args=[
                gql.Argument(name='filter', type=gql.Ref('GlossaryTermTargetFilter'))
            ],
            resolver=resolve_term_associations,
            type=gql.Ref('TermLinkSearchResults'),
        ),
    ],
)

TermLinkSearchResults = gql.ObjectType(
    name='TermLinkSearchResults',
    fields=[
        gql.Field(name='count', type=gql.Integer),
        gql.Field(name='page', type=gql.Integer),
        gql.Field(name='pages', type=gql.Integer),
        gql.Field(name='hasNext', type=gql.Boolean),
        gql.Field(name='hasPrevious', type=gql.Boolean),
        gql.Field(name='nodes', type=gql.ArrayType(gql.Ref('GlossaryTermLink'))),
    ],
)


TermSearchResult = gql.ObjectType(
    name='TermSearchResult',
    fields=[
        gql.Field(name='count', type=gql.Integer),
        gql.Field(name='page', type=gql.Integer),
        gql.Field(name='pages', type=gql.Integer),
        gql.Field(name='hasNext', type=gql.Boolean),
        gql.Field(name='hasPrevious', type=gql.Boolean),
        gql.Field(name='nodes', type=gql.ArrayType(gql.Ref('Term'))),
    ],
)


CategorySearchResult = gql.ObjectType(
    name='CategorySearchResult',
    fields=[
        gql.Field(name='count', type=gql.Integer),
        gql.Field(name='page', type=gql.Integer),
        gql.Field(name='pages', type=gql.Integer),
        gql.Field(name='hasNext', type=gql.Boolean),
        gql.Field(name='hasPrevious', type=gql.Boolean),
        gql.Field(name='nodes', type=gql.ArrayType(gql.Ref('Category'))),
    ],
)


GlossarySearchResult = gql.ObjectType(
    name='GlossarySearchResult',
    fields=[
        gql.Field(name='count', type=gql.Integer),
        gql.Field(name='page', type=gql.Integer),
        gql.Field(name='pages', type=gql.Integer),
        gql.Field(name='hasNext', type=gql.Boolean),
        gql.Field(name='hasPrevious', type=gql.Boolean),
        gql.Field(name='nodes', type=gql.ArrayType(gql.Ref('Glossary'))),
    ],
)

GlossaryTermLinkTarget = gql.Union(
    name='GlossaryTermLinkTarget',
    types=[
        gql.Ref('Dataset'),
        gql.Ref('DatasetTable'),
        gql.Ref('DatasetStorageLocation'),
        gql.Ref('DatasetTableColumn'),
        gql.Ref('Dashboard'),
    ],
    resolver=target_union_resolver,
)

GlossaryTermLink = gql.ObjectType(
    'GlossaryTermLink',
    fields=[
        gql.Field(name='linkUri', type=gql.ID),
        gql.Field(name='created', type=gql.NonNullableType(gql.String)),
        gql.Field(name='updated', type=gql.String),
        gql.Field(name='deleted', type=gql.String),
        gql.Field(name='owner', type=gql.String),
        gql.Field(name='nodeUri', type=gql.NonNullableType(gql.String)),
        gql.Field(name='targetUri', type=gql.NonNullableType(gql.String)),
        gql.Field(name='targetType', type=gql.NonNullableType(gql.String)),
        gql.Field(name='approvedByOwner', type=gql.NonNullableType(gql.Boolean)),
        gql.Field(name='approvedBySteward', type=gql.NonNullableType(gql.Boolean)),
        gql.Field(name='term', resolver=resolve_link_node, type=gql.Ref('Term')),
        gql.Field(
            name='target',
            resolver=resolve_link_target,
            type=gql.Ref('GlossaryTermLinkTarget'),
        ),
    ],
)


GlossaryNodeStatistics = gql.ObjectType(
    name='GlossaryNodeStatistics',
    fields=[
        gql.Field(name='categories', type=gql.Integer),
        gql.Field(name='terms', type=gql.Integer),
        gql.Field(name='associations', type=gql.Integer),
    ],
)
