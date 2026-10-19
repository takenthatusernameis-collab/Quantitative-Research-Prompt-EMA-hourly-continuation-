# EMA Hourly Continuation — DOGE/USDT P21_34

**Symbol:** DOGE/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1106 |
| net_profit_factor | 0.2856 |
| net_win_rate | 0.3942 |
| gross_profit_factor | 0.7475 |
| gross_win_rate | 0.4340 |
| sharpe_ratio | -12.0466 |
| sortino_ratio | -5.7198 |
| max_drawdown | 0.9995 |
| cagr | -0.9508 |
| net_avg_win | 9.1642 |
| net_avg_loss | -20.8812 |
| avg_hold_time_bars | 2.4295 |
| exposure | 0.1221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
