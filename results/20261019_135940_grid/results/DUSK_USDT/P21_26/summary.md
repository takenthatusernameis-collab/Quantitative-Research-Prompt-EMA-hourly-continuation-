# EMA Hourly Continuation — DUSK/USDT P21_26

**Symbol:** DUSK/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1118 |
| net_profit_factor | 0.3478 |
| net_win_rate | 0.3998 |
| gross_profit_factor | 1.0561 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -11.4384 |
| sortino_ratio | -5.4749 |
| max_drawdown | 0.9992 |
| cagr | -0.9400 |
| net_avg_win | 11.9189 |
| net_avg_loss | -22.8304 |
| avg_hold_time_bars | 2.0635 |
| exposure | 0.1049 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
