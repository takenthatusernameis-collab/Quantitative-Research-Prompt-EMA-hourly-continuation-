# EMA Hourly Continuation — AXS/USDT P12_21

**Symbol:** AXS/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.7674 |
| net_win_rate | 0.5318 |
| gross_profit_factor | 1.1307 |
| gross_win_rate | 0.5318 |
| sharpe_ratio | -1.4015 |
| sortino_ratio | -0.3494 |
| max_drawdown | 0.3476 |
| cagr | -0.1481 |
| net_avg_win | 68.9987 |
| net_avg_loss | -102.1152 |
| avg_hold_time_bars | 5.3378 |
| exposure | 0.0722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
