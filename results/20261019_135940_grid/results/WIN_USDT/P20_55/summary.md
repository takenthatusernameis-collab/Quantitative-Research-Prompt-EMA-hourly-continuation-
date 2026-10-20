# EMA Hourly Continuation — WIN/USDT P20_55

**Symbol:** WIN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 894 |
| net_profit_factor | 0.3551 |
| net_win_rate | 0.4016 |
| gross_profit_factor | 0.8070 |
| gross_win_rate | 0.4273 |
| sharpe_ratio | -9.6733 |
| sortino_ratio | -4.0982 |
| max_drawdown | 0.9952 |
| cagr | -0.8794 |
| net_avg_win | 15.2644 |
| net_avg_loss | -28.8423 |
| avg_hold_time_bars | 5.6734 |
| exposure | 0.2305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
