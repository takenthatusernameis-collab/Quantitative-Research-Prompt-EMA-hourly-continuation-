# EMA Hourly Continuation — AIOZ/USDT P8_26

**Symbol:** AIOZ/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 622 |
| net_profit_factor | 0.7270 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.9210 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -2.7381 |
| sortino_ratio | -0.9741 |
| max_drawdown | 0.6928 |
| cagr | -0.3610 |
| net_avg_win | 60.7533 |
| net_avg_loss | -75.8758 |
| avg_hold_time_bars | 6.7460 |
| exposure | 0.1907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
