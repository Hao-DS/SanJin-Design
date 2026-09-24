import { Layout, Nav, Typography } from '@douyinfe/semi-ui';

/** Semi Layout.Sider 默认 200，Nav 默认 240。两侧必须同宽，否则导航横向溢出。 */
const SIDE_WIDTH = 240;

export default function App() {
  return (
    <Layout className="shell">
      <Layout.Sider className="shell__side" width={SIDE_WIDTH}>
        <div className="brand">原型</div>
        <Nav
          style={{ width: SIDE_WIDTH }}
          items={[{ itemKey: 'home', text: '首页' }]}
          selectedKeys={['home']}
        />
      </Layout.Sider>
      <Layout.Content className="shell__body">
        <div className="page">
          <header className="page__head">
            <div>
              <Typography.Title heading={4} className="page__title">
                页面标题
              </Typography.Title>
              <p className="page__meta">数据范围与更新时间放这里</p>
            </div>
          </header>
          <div className="filter-bar">筛选条与标题左缘对齐，不要再包一层 padding</div>
          <div className="table-panel">主表或主图放这里，与筛选条同宽</div>
        </div>
      </Layout.Content>
    </Layout>
  );
}
