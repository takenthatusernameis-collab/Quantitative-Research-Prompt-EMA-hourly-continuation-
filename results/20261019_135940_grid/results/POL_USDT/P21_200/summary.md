# EMA Hourly Continuation — POL/USDT P21_200

**Symbol:** POL/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.6790 |
| net_win_rate | 0.4888 |
| gross_profit_factor | 0.9645 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.0281 |
| sortino_ratio | -0.5415 |
| max_drawdown | 0.5486 |
| cagr | -0.2257 |
| net_avg_win | 57.6259 |
| net_avg_loss | -81.1331 |
| avg_hold_time_bars | 41.3764 |
| exposure | 0.6695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
