# EMA Hourly Continuation — LPT/USDT P8_200

**Symbol:** LPT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.6540 |
| net_win_rate | 0.4657 |
| gross_profit_factor | 0.8726 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -2.7045 |
| sortino_ratio | -0.7812 |
| max_drawdown | 0.6295 |
| cagr | -0.3076 |
| net_avg_win | 57.8332 |
| net_avg_loss | -77.0813 |
| avg_hold_time_bars | 40.7447 |
| exposure | 0.7834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
