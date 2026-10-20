# EMA Hourly Continuation — BLUR/USDT P8_26

**Symbol:** BLUR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1494 |
| net_profit_factor | 0.4709 |
| net_win_rate | 0.4317 |
| gross_profit_factor | 0.8585 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -9.6893 |
| sortino_ratio | -5.2335 |
| max_drawdown | 0.9986 |
| cagr | -0.9252 |
| net_avg_win | 13.7784 |
| net_avg_loss | -22.2293 |
| avg_hold_time_bars | 4.0810 |
| exposure | 0.2759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
