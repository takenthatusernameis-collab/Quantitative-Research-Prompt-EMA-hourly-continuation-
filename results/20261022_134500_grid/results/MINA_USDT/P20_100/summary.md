# EMA Hourly Continuation — MINA/USDT P20_100

**Symbol:** MINA/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.6678 |
| net_win_rate | 0.4892 |
| gross_profit_factor | 0.9901 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -3.0905 |
| sortino_ratio | -1.0671 |
| max_drawdown | 0.7610 |
| cagr | -0.4012 |
| net_avg_win | 49.5226 |
| net_avg_loss | -71.0145 |
| avg_hold_time_bars | 18.4176 |
| exposure | 0.5031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
