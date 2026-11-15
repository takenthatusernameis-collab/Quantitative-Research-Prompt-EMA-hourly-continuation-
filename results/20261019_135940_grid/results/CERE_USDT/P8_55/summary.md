# EMA Hourly Continuation — CERE/USDT P8_55

**Symbol:** CERE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1140 |
| net_profit_factor | 0.4129 |
| net_win_rate | 0.3570 |
| gross_profit_factor | 0.6859 |
| gross_win_rate | 0.3833 |
| sharpe_ratio | -12.0889 |
| sortino_ratio | -5.7428 |
| max_drawdown | 0.9995 |
| cagr | -0.9492 |
| net_avg_win | 17.2671 |
| net_avg_loss | -23.2225 |
| avg_hold_time_bars | 9.2640 |
| exposure | 0.4800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
