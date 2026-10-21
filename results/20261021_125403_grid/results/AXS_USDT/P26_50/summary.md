# EMA Hourly Continuation — AXS/USDT P26_50

**Symbol:** AXS/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.8723 |
| net_win_rate | 0.5505 |
| gross_profit_factor | 1.2177 |
| gross_win_rate | 0.5505 |
| sharpe_ratio | -0.8008 |
| sortino_ratio | -0.2250 |
| max_drawdown | 0.3052 |
| cagr | -0.0999 |
| net_avg_win | 76.9328 |
| net_avg_loss | -108.0263 |
| avg_hold_time_bars | 6.2394 |
| exposure | 0.1062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
