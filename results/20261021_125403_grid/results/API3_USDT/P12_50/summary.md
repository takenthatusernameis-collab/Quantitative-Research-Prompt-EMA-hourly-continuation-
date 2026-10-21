# EMA Hourly Continuation — API3/USDT P12_50

**Symbol:** API3/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.7519 |
| net_win_rate | 0.4888 |
| gross_profit_factor | 0.9671 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -2.5376 |
| sortino_ratio | -0.9369 |
| max_drawdown | 0.6840 |
| cagr | -0.3497 |
| net_avg_win | 61.4116 |
| net_avg_loss | -78.0850 |
| avg_hold_time_bars | 11.0780 |
| exposure | 0.3359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
