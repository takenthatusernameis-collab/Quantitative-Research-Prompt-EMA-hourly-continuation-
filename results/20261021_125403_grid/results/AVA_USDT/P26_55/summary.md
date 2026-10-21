# EMA Hourly Continuation — AVA/USDT P26_55

**Symbol:** AVA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.7586 |
| net_win_rate | 0.5141 |
| gross_profit_factor | 1.0388 |
| gross_win_rate | 0.5141 |
| sharpe_ratio | -1.7162 |
| sortino_ratio | -0.5099 |
| max_drawdown | 0.4743 |
| cagr | -0.2080 |
| net_avg_win | 63.5859 |
| net_avg_loss | -88.6807 |
| avg_hold_time_bars | 6.9624 |
| exposure | 0.1348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
