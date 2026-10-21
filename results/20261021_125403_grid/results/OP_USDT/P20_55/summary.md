# EMA Hourly Continuation — OP/USDT P20_55

**Symbol:** OP/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.7519 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9856 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.9186 |
| sortino_ratio | -0.6162 |
| max_drawdown | 0.5156 |
| cagr | -0.2464 |
| net_avg_win | 61.3937 |
| net_avg_loss | -81.6551 |
| avg_hold_time_bars | 9.1494 |
| exposure | 0.2088 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
