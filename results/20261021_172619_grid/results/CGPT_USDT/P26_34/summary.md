# EMA Hourly Continuation — CGPT/USDT P26_34

**Symbol:** CGPT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 179 |
| net_profit_factor | 0.7406 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 1.0237 |
| gross_win_rate | 0.5028 |
| sharpe_ratio | -1.3288 |
| sortino_ratio | -0.2554 |
| max_drawdown | 0.3101 |
| cagr | -0.1102 |
| net_avg_win | 80.6112 |
| net_avg_loss | -110.0747 |
| avg_hold_time_bars | 5.1788 |
| exposure | 0.0421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
