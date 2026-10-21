# EMA Hourly Continuation — CPOOL/USDT P55_100

**Symbol:** CPOOL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.7596 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9361 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -1.6651 |
| sortino_ratio | -0.4315 |
| max_drawdown | 0.4470 |
| cagr | -0.1805 |
| net_avg_win | 78.1804 |
| net_avg_loss | -95.6959 |
| avg_hold_time_bars | 6.2455 |
| exposure | 0.0937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
