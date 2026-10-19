# EMA Hourly Continuation — DOGE/USDT P26_55

**Symbol:** DOGE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 905 |
| net_profit_factor | 0.3477 |
| net_win_rate | 0.4188 |
| gross_profit_factor | 0.7427 |
| gross_win_rate | 0.4464 |
| sharpe_ratio | -8.9731 |
| sortino_ratio | -3.8234 |
| max_drawdown | 0.9918 |
| cagr | -0.8522 |
| net_avg_win | 13.9500 |
| net_avg_loss | -28.9067 |
| avg_hold_time_bars | 4.2575 |
| exposure | 0.1751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
