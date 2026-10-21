# EMA Hourly Continuation — FIL/USDT P34_200

**Symbol:** FIL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.7947 |
| net_win_rate | 0.4910 |
| gross_profit_factor | 0.9607 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -1.1929 |
| sortino_ratio | -0.2845 |
| max_drawdown | 0.3215 |
| cagr | -0.1235 |
| net_avg_win | 79.6084 |
| net_avg_loss | -96.6498 |
| avg_hold_time_bars | 39.8029 |
| exposure | 0.5048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
