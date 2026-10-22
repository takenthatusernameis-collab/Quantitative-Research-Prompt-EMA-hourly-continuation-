# EMA Hourly Continuation — GTC/USDT P144_200

**Symbol:** GTC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.6281 |
| net_win_rate | 0.4593 |
| gross_profit_factor | 0.8578 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -2.3645 |
| sortino_ratio | -0.5281 |
| max_drawdown | 0.4705 |
| cagr | -0.2148 |
| net_avg_win | 68.0345 |
| net_avg_loss | -92.0289 |
| avg_hold_time_bars | 7.5854 |
| exposure | 0.0848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
