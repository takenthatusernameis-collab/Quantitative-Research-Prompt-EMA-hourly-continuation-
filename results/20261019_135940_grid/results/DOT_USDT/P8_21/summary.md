# EMA Hourly Continuation — DOT/USDT P8_21

**Symbol:** DOT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1707 |
| net_profit_factor | 0.2940 |
| net_win_rate | 0.4282 |
| gross_profit_factor | 0.8379 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -13.2167 |
| sortino_ratio | -7.7283 |
| max_drawdown | 1.0000 |
| cagr | -0.9813 |
| net_avg_win | 5.6963 |
| net_avg_loss | -14.5118 |
| avg_hold_time_bars | 2.8325 |
| exposure | 0.2198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
