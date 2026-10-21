# EMA Hourly Continuation — AVA/USDT P21_55

**Symbol:** AVA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7686 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0342 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -1.7679 |
| sortino_ratio | -0.5607 |
| max_drawdown | 0.4989 |
| cagr | -0.2263 |
| net_avg_win | 63.3534 |
| net_avg_loss | -86.6034 |
| avg_hold_time_bars | 7.7387 |
| exposure | 0.1710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
