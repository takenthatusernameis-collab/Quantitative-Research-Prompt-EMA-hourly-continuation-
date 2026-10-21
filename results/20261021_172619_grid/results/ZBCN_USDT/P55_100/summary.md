# EMA Hourly Continuation — ZBCN/USDT P55_100

**Symbol:** ZBCN/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.7304 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.8989 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -1.5721 |
| sortino_ratio | -0.3893 |
| max_drawdown | 0.3937 |
| cagr | -0.1641 |
| net_avg_win | 68.1867 |
| net_avg_loss | -86.0783 |
| avg_hold_time_bars | 6.0270 |
| exposure | 0.0825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
