# EMA Hourly Continuation — CRO/USDT P26_100

**Symbol:** CRO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.4606 |
| net_win_rate | 0.4387 |
| gross_profit_factor | 0.9194 |
| gross_win_rate | 0.4675 |
| sharpe_ratio | -6.3324 |
| sortino_ratio | -2.2763 |
| max_drawdown | 0.9487 |
| cagr | -0.6839 |
| net_avg_win | 27.8091 |
| net_avg_loss | -47.1970 |
| avg_hold_time_bars | 12.2148 |
| exposure | 0.3670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
