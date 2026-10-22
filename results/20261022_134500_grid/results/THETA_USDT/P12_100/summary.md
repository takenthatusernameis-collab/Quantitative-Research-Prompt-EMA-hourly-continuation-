# EMA Hourly Continuation — THETA/USDT P12_100

**Symbol:** THETA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.6431 |
| net_win_rate | 0.4642 |
| gross_profit_factor | 0.9221 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -3.5872 |
| sortino_ratio | -1.2271 |
| max_drawdown | 0.7810 |
| cagr | -0.4382 |
| net_avg_win | 50.6738 |
| net_avg_loss | -68.2578 |
| avg_hold_time_bars | 23.0495 |
| exposure | 0.6140 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
