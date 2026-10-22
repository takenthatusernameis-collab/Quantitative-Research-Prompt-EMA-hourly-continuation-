# EMA Hourly Continuation — PIXEL/USDT P100_144

**Symbol:** PIXEL/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.5870 |
| net_win_rate | 0.4602 |
| gross_profit_factor | 0.9349 |
| gross_win_rate | 0.4712 |
| sharpe_ratio | -4.0891 |
| sortino_ratio | -1.2271 |
| max_drawdown | 0.7860 |
| cagr | -0.4443 |
| net_avg_win | 52.8058 |
| net_avg_loss | -76.6868 |
| avg_hold_time_bars | 4.4602 |
| exposure | 0.0912 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
