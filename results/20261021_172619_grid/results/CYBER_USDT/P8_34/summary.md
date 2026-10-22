# EMA Hourly Continuation — CYBER/USDT P8_34

**Symbol:** CYBER/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 826 |
| net_profit_factor | 0.7247 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9671 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -3.1423 |
| sortino_ratio | -1.2918 |
| max_drawdown | 0.7815 |
| cagr | -0.4468 |
| net_avg_win | 50.2903 |
| net_avg_loss | -66.7616 |
| avg_hold_time_bars | 8.7591 |
| exposure | 0.3289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
