# EMA Hourly Continuation — AERO/USDT P8_21

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1607 |
| net_profit_factor | 0.3808 |
| net_win_rate | 0.4356 |
| gross_profit_factor | 0.7434 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -10.6330 |
| sortino_ratio | -5.9719 |
| max_drawdown | 0.9995 |
| cagr | -0.9511 |
| net_avg_win | 8.7819 |
| net_avg_loss | -17.7973 |
| avg_hold_time_bars | 3.0336 |
| exposure | 0.2216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
