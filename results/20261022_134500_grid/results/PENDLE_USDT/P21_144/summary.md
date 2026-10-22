# EMA Hourly Continuation — PENDLE/USDT P21_144

**Symbol:** PENDLE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.6008 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.8733 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -3.4480 |
| sortino_ratio | -1.0686 |
| max_drawdown | 0.7466 |
| cagr | -0.4033 |
| net_avg_win | 48.1688 |
| net_avg_loss | -68.4212 |
| avg_hold_time_bars | 25.8560 |
| exposure | 0.5794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
