# EMA Hourly Continuation — IMX/USDT P50_200

**Symbol:** IMX/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.8192 |
| net_win_rate | 0.5341 |
| gross_profit_factor | 1.1275 |
| gross_win_rate | 0.5341 |
| sharpe_ratio | -1.0633 |
| sortino_ratio | -0.2819 |
| max_drawdown | 0.3180 |
| cagr | -0.1277 |
| net_avg_win | 70.2528 |
| net_avg_loss | -98.3093 |
| avg_hold_time_bars | 25.7585 |
| exposure | 0.4103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
