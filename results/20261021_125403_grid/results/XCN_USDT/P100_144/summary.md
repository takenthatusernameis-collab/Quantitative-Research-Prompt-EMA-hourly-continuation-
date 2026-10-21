# EMA Hourly Continuation — XCN/USDT P100_144

**Symbol:** XCN/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 237 |
| net_profit_factor | 0.6057 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8243 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -2.4413 |
| sortino_ratio | -0.5358 |
| max_drawdown | 0.4897 |
| cagr | -0.2183 |
| net_avg_win | 66.2097 |
| net_avg_loss | -89.9756 |
| avg_hold_time_bars | 7.5865 |
| exposure | 0.0817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
