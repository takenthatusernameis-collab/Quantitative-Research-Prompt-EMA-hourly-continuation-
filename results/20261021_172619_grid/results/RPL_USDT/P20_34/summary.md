# EMA Hourly Continuation — RPL/USDT P20_34

**Symbol:** RPL/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.5939 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.8564 |
| gross_win_rate | 0.4436 |
| sharpe_ratio | -4.2978 |
| sortino_ratio | -1.4111 |
| max_drawdown | 0.8064 |
| cagr | -0.4785 |
| net_avg_win | 49.9737 |
| net_avg_loss | -67.0882 |
| avg_hold_time_bars | 5.9568 |
| exposure | 0.1434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
