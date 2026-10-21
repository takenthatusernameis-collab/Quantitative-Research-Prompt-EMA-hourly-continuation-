# EMA Hourly Continuation — PUNDIX/USDT P8_100

**Symbol:** PUNDIX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.7530 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9674 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -2.4845 |
| sortino_ratio | -0.8466 |
| max_drawdown | 0.6518 |
| cagr | -0.3233 |
| net_avg_win | 69.2849 |
| net_avg_loss | -85.4840 |
| avg_hold_time_bars | 24.3940 |
| exposure | 0.6331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
