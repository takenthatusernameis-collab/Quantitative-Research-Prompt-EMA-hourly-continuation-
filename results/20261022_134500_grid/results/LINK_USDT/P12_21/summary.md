# EMA Hourly Continuation — LINK/USDT P12_21

**Symbol:** LINK/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1375 |
| net_profit_factor | 0.2895 |
| net_win_rate | 0.4065 |
| gross_profit_factor | 0.8554 |
| gross_win_rate | 0.4415 |
| sharpe_ratio | -13.6964 |
| sortino_ratio | -7.2749 |
| max_drawdown | 0.9999 |
| cagr | -0.9793 |
| net_avg_win | 7.2898 |
| net_avg_loss | -17.2480 |
| avg_hold_time_bars | 2.2371 |
| exposure | 0.1398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
