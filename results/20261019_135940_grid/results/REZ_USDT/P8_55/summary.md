# EMA Hourly Continuation — REZ/USDT P8_55

**Symbol:** REZ/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 998 |
| net_profit_factor | 0.7170 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 1.0383 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -3.8609 |
| sortino_ratio | -1.7332 |
| max_drawdown | 0.8778 |
| cagr | -0.5630 |
| net_avg_win | 44.8460 |
| net_avg_loss | -60.8194 |
| avg_hold_time_bars | 10.5812 |
| exposure | 0.4872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
