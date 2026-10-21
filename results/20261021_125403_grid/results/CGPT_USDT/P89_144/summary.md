# EMA Hourly Continuation — CGPT/USDT P89_144

**Symbol:** CGPT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.8473 |
| net_win_rate | 0.5271 |
| gross_profit_factor | 1.1135 |
| gross_win_rate | 0.5310 |
| sharpe_ratio | -0.8018 |
| sortino_ratio | -0.1858 |
| max_drawdown | 0.2597 |
| cagr | -0.0829 |
| net_avg_win | 79.7652 |
| net_avg_loss | -104.9378 |
| avg_hold_time_bars | 6.7713 |
| exposure | 0.0794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
