# EMA Hourly Continuation — UMA/USDT P20_26

**Symbol:** UMA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1165 |
| net_profit_factor | 0.2066 |
| net_win_rate | 0.3451 |
| gross_profit_factor | 0.6275 |
| gross_win_rate | 0.3966 |
| sharpe_ratio | -14.2142 |
| sortino_ratio | -7.0569 |
| max_drawdown | 0.9999 |
| cagr | -0.9755 |
| net_avg_win | 6.4757 |
| net_avg_loss | -16.5168 |
| avg_hold_time_bars | 2.6918 |
| exposure | 0.1425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
