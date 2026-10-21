# EMA Hourly Continuation — LTC/USDT P8_20

**Symbol:** LTC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.6400 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 1.0002 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -2.9462 |
| sortino_ratio | -0.8538 |
| max_drawdown | 0.6245 |
| cagr | -0.3229 |
| net_avg_win | 55.5143 |
| net_avg_loss | -84.6220 |
| avg_hold_time_bars | 5.8938 |
| exposure | 0.1085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
