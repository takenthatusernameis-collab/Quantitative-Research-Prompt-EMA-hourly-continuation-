# EMA Hourly Continuation — XAI/USDT P12_21

**Symbol:** XAI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.6297 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.8509 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -3.0551 |
| sortino_ratio | -0.8860 |
| max_drawdown | 0.6554 |
| cagr | -0.3336 |
| net_avg_win | 57.2100 |
| net_avg_loss | -77.4051 |
| avg_hold_time_bars | 4.6562 |
| exposure | 0.0874 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
