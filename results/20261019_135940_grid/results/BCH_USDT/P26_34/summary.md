# EMA Hourly Continuation — BCH/USDT P26_34

**Symbol:** BCH/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1056 |
| net_profit_factor | 0.1985 |
| net_win_rate | 0.3381 |
| gross_profit_factor | 0.6974 |
| gross_win_rate | 0.4138 |
| sharpe_ratio | -14.8137 |
| sortino_ratio | -7.1446 |
| max_drawdown | 0.9999 |
| cagr | -0.9796 |
| net_avg_win | 6.9359 |
| net_avg_loss | -17.8477 |
| avg_hold_time_bars | 2.0890 |
| exposure | 0.1003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
