# EMA Hourly Continuation — SUN/USDT P12_21

**Symbol:** SUN/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1315 |
| net_profit_factor | 0.0996 |
| net_win_rate | 0.3125 |
| gross_profit_factor | 0.5647 |
| gross_win_rate | 0.4266 |
| sharpe_ratio | -17.8859 |
| sortino_ratio | -9.7861 |
| max_drawdown | 1.0000 |
| cagr | -0.9953 |
| net_avg_win | 2.6908 |
| net_avg_loss | -12.2853 |
| avg_hold_time_bars | 3.4114 |
| exposure | 0.2030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
