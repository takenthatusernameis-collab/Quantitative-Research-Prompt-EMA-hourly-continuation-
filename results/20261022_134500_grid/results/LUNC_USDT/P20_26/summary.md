# EMA Hourly Continuation — LUNC/USDT P20_26

**Symbol:** LUNC/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1267 |
| net_profit_factor | 0.1729 |
| net_win_rate | 0.3173 |
| gross_profit_factor | 0.6392 |
| gross_win_rate | 0.3741 |
| sharpe_ratio | -16.8058 |
| sortino_ratio | -8.8771 |
| max_drawdown | 1.0000 |
| cagr | -0.9918 |
| net_avg_win | 5.2006 |
| net_avg_loss | -13.9775 |
| avg_hold_time_bars | 1.8587 |
| exposure | 0.1070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
