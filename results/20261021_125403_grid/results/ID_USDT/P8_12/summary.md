# EMA Hourly Continuation — ID/USDT P8_12

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.6400 |
| net_win_rate | 0.5107 |
| gross_profit_factor | 1.0307 |
| gross_win_rate | 0.5107 |
| sharpe_ratio | -3.0548 |
| sortino_ratio | -0.9938 |
| max_drawdown | 0.6980 |
| cagr | -0.3653 |
| net_avg_win | 46.3001 |
| net_avg_loss | -75.5136 |
| avg_hold_time_bars | 4.6550 |
| exposure | 0.1081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
