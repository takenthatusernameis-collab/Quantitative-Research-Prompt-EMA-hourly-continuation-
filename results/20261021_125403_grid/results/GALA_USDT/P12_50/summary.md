# EMA Hourly Continuation — GALA/USDT P12_50

**Symbol:** GALA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.7515 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9538 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -2.3045 |
| sortino_ratio | -0.8162 |
| max_drawdown | 0.6339 |
| cagr | -0.3128 |
| net_avg_win | 61.7199 |
| net_avg_loss | -77.9568 |
| avg_hold_time_bars | 10.2541 |
| exposure | 0.2862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
