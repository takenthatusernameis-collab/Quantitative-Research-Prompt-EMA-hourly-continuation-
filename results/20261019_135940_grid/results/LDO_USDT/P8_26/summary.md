# EMA Hourly Continuation — LDO/USDT P8_26

**Symbol:** LDO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1584 |
| net_profit_factor | 0.3699 |
| net_win_rate | 0.4217 |
| gross_profit_factor | 0.6733 |
| gross_win_rate | 0.4388 |
| sharpe_ratio | -10.7544 |
| sortino_ratio | -6.0222 |
| max_drawdown | 0.9995 |
| cagr | -0.9503 |
| net_avg_win | 8.7845 |
| net_avg_loss | -17.3174 |
| avg_hold_time_bars | 3.8864 |
| exposure | 0.2798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
