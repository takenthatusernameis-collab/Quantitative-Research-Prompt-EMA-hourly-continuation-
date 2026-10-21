# EMA Hourly Continuation — TWT/USDT P8_34

**Symbol:** TWT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 804 |
| net_profit_factor | 0.6632 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 0.9634 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -3.3405 |
| sortino_ratio | -1.3608 |
| max_drawdown | 0.7894 |
| cagr | -0.4622 |
| net_avg_win | 38.5800 |
| net_avg_loss | -58.4586 |
| avg_hold_time_bars | 8.2127 |
| exposure | 0.3001 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
