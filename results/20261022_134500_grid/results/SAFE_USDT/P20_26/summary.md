# EMA Hourly Continuation — SAFE/USDT P20_26

**Symbol:** SAFE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1131 |
| net_profit_factor | 0.2277 |
| net_win_rate | 0.3731 |
| gross_profit_factor | 0.6817 |
| gross_win_rate | 0.4200 |
| sharpe_ratio | -12.8259 |
| sortino_ratio | -6.2192 |
| max_drawdown | 0.9997 |
| cagr | -0.9610 |
| net_avg_win | 6.9858 |
| net_avg_loss | -18.2580 |
| avg_hold_time_bars | 2.8930 |
| exposure | 0.1498 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
