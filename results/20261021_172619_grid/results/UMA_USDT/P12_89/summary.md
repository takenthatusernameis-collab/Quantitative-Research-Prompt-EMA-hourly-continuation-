# EMA Hourly Continuation — UMA/USDT P12_89

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.7759 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9902 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -1.9427 |
| sortino_ratio | -0.6599 |
| max_drawdown | 0.5600 |
| cagr | -0.2620 |
| net_avg_win | 65.7566 |
| net_avg_loss | -84.1529 |
| avg_hold_time_bars | 19.3759 |
| exposure | 0.4967 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
