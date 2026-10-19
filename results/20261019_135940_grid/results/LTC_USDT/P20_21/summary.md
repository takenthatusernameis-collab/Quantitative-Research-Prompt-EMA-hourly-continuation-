# EMA Hourly Continuation — LTC/USDT P20_21

**Symbol:** LTC/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1183 |
| net_profit_factor | 0.0749 |
| net_win_rate | 0.2511 |
| gross_profit_factor | 0.6859 |
| gross_win_rate | 0.3339 |
| sharpe_ratio | -20.4694 |
| sortino_ratio | -11.5462 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 2.7259 |
| net_avg_loss | -12.2004 |
| avg_hold_time_bars | 1.4793 |
| exposure | 0.0795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
