# EMA Hourly Continuation — ARB/USDT P20_34

**Symbol:** ARB/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1112 |
| net_profit_factor | 0.3210 |
| net_win_rate | 0.4371 |
| gross_profit_factor | 0.7968 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -9.8446 |
| sortino_ratio | -4.6300 |
| max_drawdown | 0.9974 |
| cagr | -0.9056 |
| net_avg_win | 9.7004 |
| net_avg_loss | -23.4628 |
| avg_hold_time_bars | 2.6915 |
| exposure | 0.1360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
