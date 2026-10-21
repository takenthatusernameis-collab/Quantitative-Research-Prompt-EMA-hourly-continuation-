# EMA Hourly Continuation — RLC/USDT P21_200

**Symbol:** RLC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.7719 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9194 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -1.4455 |
| sortino_ratio | -0.3754 |
| max_drawdown | 0.4303 |
| cagr | -0.1598 |
| net_avg_win | 74.9250 |
| net_avg_loss | -90.2884 |
| avg_hold_time_bars | 40.1386 |
| exposure | 0.6057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
