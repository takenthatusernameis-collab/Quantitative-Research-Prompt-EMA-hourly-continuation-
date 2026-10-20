# EMA Hourly Continuation — CSPR/USDT P8_34

**Symbol:** CSPR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1639 |
| net_profit_factor | 0.3860 |
| net_win_rate | 0.4131 |
| gross_profit_factor | 0.8104 |
| gross_win_rate | 0.4265 |
| sharpe_ratio | -11.4375 |
| sortino_ratio | -6.5121 |
| max_drawdown | 0.9997 |
| cagr | -0.9605 |
| net_avg_win | 9.2842 |
| net_avg_loss | -16.9256 |
| avg_hold_time_bars | 4.2526 |
| exposure | 0.3168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
