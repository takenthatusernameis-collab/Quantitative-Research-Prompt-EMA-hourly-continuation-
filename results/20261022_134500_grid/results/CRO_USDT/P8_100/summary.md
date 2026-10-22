# EMA Hourly Continuation — CRO/USDT P8_100

**Symbol:** CRO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.4857 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.8952 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -5.4016 |
| sortino_ratio | -1.9379 |
| max_drawdown | 0.9171 |
| cagr | -0.6229 |
| net_avg_win | 28.3839 |
| net_avg_loss | -49.4843 |
| avg_hold_time_bars | 22.2519 |
| exposure | 0.6706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
