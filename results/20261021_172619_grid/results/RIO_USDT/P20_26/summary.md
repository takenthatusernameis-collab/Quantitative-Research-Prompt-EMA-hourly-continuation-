# EMA Hourly Continuation — RIO/USDT P20_26

**Symbol:** RIO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 185 |
| net_profit_factor | 0.6755 |
| net_win_rate | 0.4432 |
| gross_profit_factor | 0.8119 |
| gross_win_rate | 0.4432 |
| sharpe_ratio | -1.7652 |
| sortino_ratio | -0.3417 |
| max_drawdown | 0.3365 |
| cagr | -0.1458 |
| net_avg_win | 82.2924 |
| net_avg_loss | -96.9826 |
| avg_hold_time_bars | 6.0865 |
| exposure | 0.0517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
