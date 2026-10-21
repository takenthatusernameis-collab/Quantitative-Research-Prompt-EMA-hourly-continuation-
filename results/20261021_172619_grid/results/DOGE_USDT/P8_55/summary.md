# EMA Hourly Continuation — DOGE/USDT P8_55

**Symbol:** DOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 673 |
| net_profit_factor | 0.7509 |
| net_win_rate | 0.4963 |
| gross_profit_factor | 0.9824 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -2.3949 |
| sortino_ratio | -0.8892 |
| max_drawdown | 0.6498 |
| cagr | -0.3356 |
| net_avg_win | 57.9457 |
| net_avg_loss | -76.0263 |
| avg_hold_time_bars | 13.0178 |
| exposure | 0.3982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
