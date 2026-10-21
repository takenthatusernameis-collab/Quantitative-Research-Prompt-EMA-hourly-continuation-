# EMA Hourly Continuation — BICO/USDT P34_100

**Symbol:** BICO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.6611 |
| net_win_rate | 0.4553 |
| gross_profit_factor | 0.8269 |
| gross_win_rate | 0.4553 |
| sharpe_ratio | -2.7574 |
| sortino_ratio | -0.8488 |
| max_drawdown | 0.6346 |
| cagr | -0.3234 |
| net_avg_win | 56.9753 |
| net_avg_loss | -72.0482 |
| avg_hold_time_bars | 13.9979 |
| exposure | 0.2990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
