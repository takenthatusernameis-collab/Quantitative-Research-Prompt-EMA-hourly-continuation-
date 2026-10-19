# EMA Hourly Continuation — XCN/USDT P34_100

**Symbol:** XCN/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 796 |
| net_profit_factor | 0.4268 |
| net_win_rate | 0.4033 |
| gross_profit_factor | 0.7897 |
| gross_win_rate | 0.4221 |
| sharpe_ratio | -8.1572 |
| sortino_ratio | -3.2095 |
| max_drawdown | 0.9842 |
| cagr | -0.8071 |
| net_avg_win | 22.8199 |
| net_avg_loss | -36.1365 |
| avg_hold_time_bars | 7.5967 |
| exposure | 0.2749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
