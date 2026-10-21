# EMA Hourly Continuation — SAND/USDT P50_144

**Symbol:** SAND/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.7118 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.8979 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -1.8282 |
| sortino_ratio | -0.4551 |
| max_drawdown | 0.4165 |
| cagr | -0.1887 |
| net_avg_win | 69.5666 |
| net_avg_loss | -88.5767 |
| avg_hold_time_bars | 22.9279 |
| exposure | 0.3179 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
