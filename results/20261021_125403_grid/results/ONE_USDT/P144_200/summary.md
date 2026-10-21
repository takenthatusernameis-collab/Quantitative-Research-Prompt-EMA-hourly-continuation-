# EMA Hourly Continuation — ONE/USDT P144_200

**Symbol:** ONE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 183 |
| net_profit_factor | 0.6899 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9015 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -1.5440 |
| sortino_ratio | -0.2984 |
| max_drawdown | 0.2991 |
| cagr | -0.1279 |
| net_avg_win | 74.3614 |
| net_avg_loss | -97.6790 |
| avg_hold_time_bars | 6.8361 |
| exposure | 0.0569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
