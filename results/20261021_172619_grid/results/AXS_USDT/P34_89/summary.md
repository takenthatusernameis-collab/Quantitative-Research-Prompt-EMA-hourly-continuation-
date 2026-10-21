# EMA Hourly Continuation — AXS/USDT P34_89

**Symbol:** AXS/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.8350 |
| net_win_rate | 0.5249 |
| gross_profit_factor | 1.1089 |
| gross_win_rate | 0.5273 |
| sharpe_ratio | -1.1724 |
| sortino_ratio | -0.3459 |
| max_drawdown | 0.3733 |
| cagr | -0.1481 |
| net_avg_win | 76.1666 |
| net_avg_loss | -100.7901 |
| avg_hold_time_bars | 11.6746 |
| exposure | 0.2224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
