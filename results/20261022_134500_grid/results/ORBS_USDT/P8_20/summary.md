# EMA Hourly Continuation — ORBS/USDT P8_20

**Symbol:** ORBS/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1593 |
| net_profit_factor | 0.2884 |
| net_win_rate | 0.3610 |
| gross_profit_factor | 0.8187 |
| gross_win_rate | 0.4036 |
| sharpe_ratio | -15.6526 |
| sortino_ratio | -8.9542 |
| max_drawdown | 1.0000 |
| cagr | -0.9904 |
| net_avg_win | 7.0467 |
| net_avg_loss | -13.8033 |
| avg_hold_time_bars | 4.3484 |
| exposure | 0.3149 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
