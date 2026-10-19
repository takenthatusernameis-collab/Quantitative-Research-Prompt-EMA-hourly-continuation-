# EMA Hourly Continuation — OP/USDT P8_200

**Symbol:** OP/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.7114 |
| net_win_rate | 0.4865 |
| gross_profit_factor | 0.9385 |
| gross_win_rate | 0.4865 |
| sharpe_ratio | -1.7936 |
| sortino_ratio | -0.4359 |
| max_drawdown | 0.4079 |
| cagr | -0.1859 |
| net_avg_win | 69.0542 |
| net_avg_loss | -91.9550 |
| avg_hold_time_bars | 61.9865 |
| exposure | 0.8340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
