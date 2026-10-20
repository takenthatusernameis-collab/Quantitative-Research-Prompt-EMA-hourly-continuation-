# EMA Hourly Continuation — FLUX/USDT P21_89

**Symbol:** FLUX/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 730 |
| net_profit_factor | 0.6315 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9951 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -3.8313 |
| sortino_ratio | -1.4606 |
| max_drawdown | 0.8335 |
| cagr | -0.5024 |
| net_avg_win | 39.7941 |
| net_avg_loss | -59.9831 |
| avg_hold_time_bars | 11.1644 |
| exposure | 0.3705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
