# EMA Hourly Continuation — ETHFI/USDT P50_55

**Symbol:** ETHFI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 90 |
| net_profit_factor | 1.2014 |
| net_win_rate | 0.6111 |
| gross_profit_factor | 1.5476 |
| gross_win_rate | 0.6111 |
| sharpe_ratio | 0.5833 |
| sortino_ratio | 0.0822 |
| max_drawdown | 0.0667 |
| cagr | 0.0333 |
| net_avg_win | 92.9884 |
| net_avg_loss | -121.6312 |
| avg_hold_time_bars | 5.6444 |
| exposure | 0.0231 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
