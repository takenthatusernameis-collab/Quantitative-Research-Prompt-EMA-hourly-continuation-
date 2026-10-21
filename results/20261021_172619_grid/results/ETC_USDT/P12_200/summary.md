# EMA Hourly Continuation — ETC/USDT P12_200

**Symbol:** ETC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.7675 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9587 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -1.3628 |
| sortino_ratio | -0.3179 |
| max_drawdown | 0.3679 |
| cagr | -0.1366 |
| net_avg_win | 77.1668 |
| net_avg_loss | -97.5852 |
| avg_hold_time_bars | 61.2873 |
| exposure | 0.7466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
