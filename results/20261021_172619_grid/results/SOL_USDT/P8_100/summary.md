# EMA Hourly Continuation — SOL/USDT P8_100

**Symbol:** SOL/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.8447 |
| net_win_rate | 0.5197 |
| gross_profit_factor | 1.0698 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -1.0996 |
| sortino_ratio | -0.3384 |
| max_drawdown | 0.3826 |
| cagr | -0.1462 |
| net_avg_win | 74.8402 |
| net_avg_loss | -95.8542 |
| avg_hold_time_bars | 29.6223 |
| exposure | 0.6167 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
