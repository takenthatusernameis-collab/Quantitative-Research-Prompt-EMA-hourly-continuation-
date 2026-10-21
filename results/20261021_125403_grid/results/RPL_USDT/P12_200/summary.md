# EMA Hourly Continuation — RPL/USDT P12_200

**Symbol:** RPL/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.9076 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0385 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -0.4799 |
| sortino_ratio | -0.1177 |
| max_drawdown | 0.2161 |
| cagr | -0.0562 |
| net_avg_win | 88.7869 |
| net_avg_loss | -101.9068 |
| avg_hold_time_bars | 58.2551 |
| exposure | 0.7751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
