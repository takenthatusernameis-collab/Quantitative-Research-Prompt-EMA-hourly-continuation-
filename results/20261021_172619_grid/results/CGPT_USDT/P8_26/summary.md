# EMA Hourly Continuation — CGPT/USDT P8_26

**Symbol:** CGPT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.8050 |
| net_win_rate | 0.5104 |
| gross_profit_factor | 1.0550 |
| gross_win_rate | 0.5104 |
| sharpe_ratio | -1.9371 |
| sortino_ratio | -0.7220 |
| max_drawdown | 0.6161 |
| cagr | -0.2825 |
| net_avg_win | 68.0662 |
| net_avg_loss | -88.1543 |
| avg_hold_time_bars | 6.3452 |
| exposure | 0.1938 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
