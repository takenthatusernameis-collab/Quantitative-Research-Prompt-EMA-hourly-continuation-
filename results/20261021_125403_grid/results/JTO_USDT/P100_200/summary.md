# EMA Hourly Continuation — JTO/USDT P100_200

**Symbol:** JTO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.6935 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8381 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -1.7851 |
| sortino_ratio | -0.4189 |
| max_drawdown | 0.4101 |
| cagr | -0.1757 |
| net_avg_win | 69.0274 |
| net_avg_loss | -85.3132 |
| avg_hold_time_bars | 12.3150 |
| exposure | 0.1528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
