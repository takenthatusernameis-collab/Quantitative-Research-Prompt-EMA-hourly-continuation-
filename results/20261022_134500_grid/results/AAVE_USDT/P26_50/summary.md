# EMA Hourly Continuation — AAVE/USDT P26_50

**Symbol:** AAVE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 971 |
| net_profit_factor | 0.4558 |
| net_win_rate | 0.4295 |
| gross_profit_factor | 0.8826 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -8.5889 |
| sortino_ratio | -3.7919 |
| max_drawdown | 0.9912 |
| cagr | -0.8467 |
| net_avg_win | 19.9077 |
| net_avg_loss | -32.8727 |
| avg_hold_time_bars | 3.4604 |
| exposure | 0.1527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
