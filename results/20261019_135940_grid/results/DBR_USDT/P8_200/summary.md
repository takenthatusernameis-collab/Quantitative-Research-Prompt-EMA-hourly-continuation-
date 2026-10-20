# EMA Hourly Continuation — DBR/USDT P8_200

**Symbol:** DBR/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.5558 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.8415 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -3.9036 |
| sortino_ratio | -1.1817 |
| max_drawdown | 0.6976 |
| cagr | -0.4371 |
| net_avg_win | 50.6770 |
| net_avg_loss | -74.8019 |
| avg_hold_time_bars | 34.0427 |
| exposure | 0.7260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
