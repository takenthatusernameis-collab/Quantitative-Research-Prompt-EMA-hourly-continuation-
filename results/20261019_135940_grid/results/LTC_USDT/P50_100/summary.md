# EMA Hourly Continuation — LTC/USDT P50_100

**Symbol:** LTC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.2955 |
| net_win_rate | 0.4015 |
| gross_profit_factor | 0.7577 |
| gross_win_rate | 0.4409 |
| sharpe_ratio | -8.1337 |
| sortino_ratio | -2.9799 |
| max_drawdown | 0.9773 |
| cagr | -0.7759 |
| net_avg_win | 15.4595 |
| net_avg_loss | -35.0965 |
| avg_hold_time_bars | 5.8303 |
| exposure | 0.1749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
