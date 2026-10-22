# EMA Hourly Continuation — MNT/USDT P8_21

**Symbol:** MNT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1631 |
| net_profit_factor | 0.2436 |
| net_win_rate | 0.3906 |
| gross_profit_factor | 0.7113 |
| gross_win_rate | 0.4445 |
| sharpe_ratio | -14.6597 |
| sortino_ratio | -8.4265 |
| max_drawdown | 1.0000 |
| cagr | -0.9879 |
| net_avg_win | 5.0563 |
| net_avg_loss | -13.3005 |
| avg_hold_time_bars | 3.6045 |
| exposure | 0.2672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
