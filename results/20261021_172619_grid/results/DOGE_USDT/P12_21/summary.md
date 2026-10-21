# EMA Hourly Continuation — DOGE/USDT P12_21

**Symbol:** DOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.6271 |
| net_win_rate | 0.4781 |
| gross_profit_factor | 0.8886 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -2.1883 |
| sortino_ratio | -0.4967 |
| max_drawdown | 0.4551 |
| cagr | -0.2036 |
| net_avg_win | 61.0285 |
| net_avg_loss | -89.1459 |
| avg_hold_time_bars | 4.7809 |
| exposure | 0.0545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
