# EMA Hourly Continuation — MERL/USDT P20_100

**Symbol:** MERL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.6779 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.9123 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -3.4063 |
| sortino_ratio | -1.2215 |
| max_drawdown | 0.7995 |
| cagr | -0.4400 |
| net_avg_win | 53.3748 |
| net_avg_loss | -68.7230 |
| avg_hold_time_bars | 14.9167 |
| exposure | 0.4406 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
