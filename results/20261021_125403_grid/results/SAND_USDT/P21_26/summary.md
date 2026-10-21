# EMA Hourly Continuation — SAND/USDT P21_26

**Symbol:** SAND/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 145 |
| net_profit_factor | 0.5891 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.8592 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -1.9764 |
| sortino_ratio | -0.3407 |
| max_drawdown | 0.3642 |
| cagr | -0.1452 |
| net_avg_win | 69.6775 |
| net_avg_loss | -101.5972 |
| avg_hold_time_bars | 4.2759 |
| exposure | 0.0282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
