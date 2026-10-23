# EMA Hourly Continuation — IO/USDT P55_100

**Symbol:** IO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.4860 |
| net_win_rate | 0.4307 |
| gross_profit_factor | 0.7471 |
| gross_win_rate | 0.4339 |
| sharpe_ratio | -5.5790 |
| sortino_ratio | -2.0136 |
| max_drawdown | 0.8995 |
| cagr | -0.6174 |
| net_avg_win | 32.0974 |
| net_avg_loss | -49.9587 |
| avg_hold_time_bars | 4.5498 |
| exposure | 0.1350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
