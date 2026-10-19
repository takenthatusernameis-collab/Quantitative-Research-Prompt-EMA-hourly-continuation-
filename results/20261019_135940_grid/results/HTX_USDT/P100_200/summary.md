# EMA Hourly Continuation — HTX/USDT P100_200

**Symbol:** HTX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.2909 |
| net_win_rate | 0.3404 |
| gross_profit_factor | 0.7379 |
| gross_win_rate | 0.3688 |
| sharpe_ratio | -8.8159 |
| sortino_ratio | -2.6463 |
| max_drawdown | 0.9725 |
| cagr | -0.7576 |
| net_avg_win | 27.6963 |
| net_avg_loss | -49.1325 |
| avg_hold_time_bars | 10.0284 |
| exposure | 0.1920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
