# EMA Hourly Continuation — IMX/USDT P144_200

**Symbol:** IMX/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 209 |
| net_profit_factor | 1.0095 |
| net_win_rate | 0.5742 |
| gross_profit_factor | 1.3354 |
| gross_win_rate | 0.5742 |
| sharpe_ratio | 0.0870 |
| sortino_ratio | 0.0184 |
| max_drawdown | 0.1465 |
| cagr | 0.0038 |
| net_avg_win | 85.1314 |
| net_avg_loss | -113.7078 |
| avg_hold_time_bars | 7.3828 |
| exposure | 0.0698 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
