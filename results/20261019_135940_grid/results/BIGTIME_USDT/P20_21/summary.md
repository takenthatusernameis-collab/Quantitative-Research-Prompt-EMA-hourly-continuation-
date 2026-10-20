# EMA Hourly Continuation — BIGTIME/USDT P20_21

**Symbol:** BIGTIME/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1218 |
| net_profit_factor | 0.1665 |
| net_win_rate | 0.3071 |
| gross_profit_factor | 0.5700 |
| gross_win_rate | 0.3949 |
| sharpe_ratio | -16.7345 |
| sortino_ratio | -8.6079 |
| max_drawdown | 1.0000 |
| cagr | -0.9919 |
| net_avg_win | 5.3405 |
| net_avg_loss | -14.2148 |
| avg_hold_time_bars | 2.1067 |
| exposure | 0.1161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
