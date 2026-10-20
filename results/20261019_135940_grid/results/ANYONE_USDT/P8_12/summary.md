# EMA Hourly Continuation — ANYONE/USDT P8_12

**Symbol:** ANYONE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1573 |
| net_profit_factor | 0.3617 |
| net_win_rate | 0.3967 |
| gross_profit_factor | 0.7718 |
| gross_win_rate | 0.4209 |
| sharpe_ratio | -13.4826 |
| sortino_ratio | -7.9632 |
| max_drawdown | 0.9999 |
| cagr | -0.9822 |
| net_avg_win | 9.0787 |
| net_avg_loss | -16.5058 |
| avg_hold_time_bars | 2.3204 |
| exposure | 0.1844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
