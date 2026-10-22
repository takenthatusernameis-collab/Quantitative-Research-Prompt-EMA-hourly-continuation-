# EMA Hourly Continuation — FLUX/USDT P21_100

**Symbol:** FLUX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.8009 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 1.0034 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -1.5206 |
| sortino_ratio | -0.4778 |
| max_drawdown | 0.4513 |
| cagr | -0.1983 |
| net_avg_win | 71.0981 |
| net_avg_loss | -89.1400 |
| avg_hold_time_bars | 18.0291 |
| exposure | 0.3942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
