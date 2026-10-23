# EMA Hourly Continuation — BLZ/USDT P20_55

**Symbol:** BLZ/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1019 |
| net_profit_factor | 0.4698 |
| net_win_rate | 0.4073 |
| gross_profit_factor | 0.8073 |
| gross_win_rate | 0.4249 |
| sharpe_ratio | -8.4725 |
| sortino_ratio | -3.8082 |
| max_drawdown | 0.9906 |
| cagr | -0.8428 |
| net_avg_win | 21.1480 |
| net_avg_loss | -30.9312 |
| avg_hold_time_bars | 5.8695 |
| exposure | 0.2707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
