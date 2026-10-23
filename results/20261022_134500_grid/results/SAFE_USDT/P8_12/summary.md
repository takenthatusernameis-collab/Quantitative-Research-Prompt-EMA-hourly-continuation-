# EMA Hourly Continuation — SAFE/USDT P8_12

**Symbol:** SAFE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1694 |
| net_profit_factor | 0.2391 |
| net_win_rate | 0.3689 |
| gross_profit_factor | 0.7784 |
| gross_win_rate | 0.4126 |
| sharpe_ratio | -16.4616 |
| sortino_ratio | -9.7710 |
| max_drawdown | 1.0000 |
| cagr | -0.9944 |
| net_avg_win | 5.0275 |
| net_avg_loss | -12.2939 |
| avg_hold_time_bars | 2.2769 |
| exposure | 0.1766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
