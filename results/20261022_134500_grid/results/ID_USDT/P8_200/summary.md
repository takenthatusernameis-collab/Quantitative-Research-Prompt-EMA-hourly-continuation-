# EMA Hourly Continuation — ID/USDT P8_200

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.6842 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9989 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -2.2836 |
| sortino_ratio | -0.6341 |
| max_drawdown | 0.5675 |
| cagr | -0.2663 |
| net_avg_win | 60.5428 |
| net_avg_loss | -82.9314 |
| avg_hold_time_bars | 43.0249 |
| exposure | 0.7808 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
