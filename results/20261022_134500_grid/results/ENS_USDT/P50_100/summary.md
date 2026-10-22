# EMA Hourly Continuation — ENS/USDT P50_100

**Symbol:** ENS/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.4992 |
| net_win_rate | 0.4534 |
| gross_profit_factor | 0.8534 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -5.5988 |
| sortino_ratio | -2.0145 |
| max_drawdown | 0.9202 |
| cagr | -0.6289 |
| net_avg_win | 30.7740 |
| net_avg_loss | -51.1459 |
| avg_hold_time_bars | 6.1328 |
| exposure | 0.1826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
