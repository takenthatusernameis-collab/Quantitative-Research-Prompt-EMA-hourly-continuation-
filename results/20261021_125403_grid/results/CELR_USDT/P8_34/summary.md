# EMA Hourly Continuation — CELR/USDT P8_34

**Symbol:** CELR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 856 |
| net_profit_factor | 0.6677 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8885 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -3.9229 |
| sortino_ratio | -1.6323 |
| max_drawdown | 0.8497 |
| cagr | -0.5267 |
| net_avg_win | 42.7294 |
| net_avg_loss | -55.8730 |
| avg_hold_time_bars | 8.2348 |
| exposure | 0.3190 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
