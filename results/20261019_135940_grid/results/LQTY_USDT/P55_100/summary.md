# EMA Hourly Continuation — LQTY/USDT P55_100

**Symbol:** LQTY/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.4680 |
| net_win_rate | 0.4347 |
| gross_profit_factor | 0.7859 |
| gross_win_rate | 0.4514 |
| sharpe_ratio | -5.8031 |
| sortino_ratio | -2.1059 |
| max_drawdown | 0.9212 |
| cagr | -0.6322 |
| net_avg_win | 28.2914 |
| net_avg_loss | -46.4768 |
| avg_hold_time_bars | 5.3967 |
| exposure | 0.1607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
