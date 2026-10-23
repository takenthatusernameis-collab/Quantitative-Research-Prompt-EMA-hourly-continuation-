# EMA Hourly Continuation — WIN/USDT P20_34

**Symbol:** WIN/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1076 |
| net_profit_factor | 0.2432 |
| net_win_rate | 0.3671 |
| gross_profit_factor | 0.7594 |
| gross_win_rate | 0.4006 |
| sharpe_ratio | -13.6532 |
| sortino_ratio | -6.5708 |
| max_drawdown | 0.9998 |
| cagr | -0.9683 |
| net_avg_win | 8.1336 |
| net_avg_loss | -19.3995 |
| avg_hold_time_bars | 2.8922 |
| exposure | 0.1415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
