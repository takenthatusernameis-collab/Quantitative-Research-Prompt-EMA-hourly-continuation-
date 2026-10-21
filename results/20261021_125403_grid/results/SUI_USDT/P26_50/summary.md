# EMA Hourly Continuation — SUI/USDT P26_50

**Symbol:** SUI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.8287 |
| net_win_rate | 0.5225 |
| gross_profit_factor | 1.0956 |
| gross_win_rate | 0.5225 |
| sharpe_ratio | -1.1470 |
| sortino_ratio | -0.3120 |
| max_drawdown | 0.3807 |
| cagr | -0.1341 |
| net_avg_win | 78.8840 |
| net_avg_loss | -104.1523 |
| avg_hold_time_bars | 6.1798 |
| exposure | 0.1000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
