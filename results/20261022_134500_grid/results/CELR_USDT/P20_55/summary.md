# EMA Hourly Continuation — CELR/USDT P20_55

**Symbol:** CELR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 938 |
| net_profit_factor | 0.5683 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.9812 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -5.3674 |
| sortino_ratio | -2.3241 |
| max_drawdown | 0.9390 |
| cagr | -0.6664 |
| net_avg_win | 27.5464 |
| net_avg_loss | -44.3141 |
| avg_hold_time_bars | 6.4382 |
| exposure | 0.2733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
