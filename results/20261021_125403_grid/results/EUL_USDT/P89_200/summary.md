# EMA Hourly Continuation — EUL/USDT P89_200

**Symbol:** EUL/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.6715 |
| net_win_rate | 0.4601 |
| gross_profit_factor | 0.8399 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -1.9050 |
| sortino_ratio | -0.4386 |
| max_drawdown | 0.4078 |
| cagr | -0.1822 |
| net_avg_win | 66.9888 |
| net_avg_loss | -85.0128 |
| avg_hold_time_bars | 14.4221 |
| exposure | 0.1724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
