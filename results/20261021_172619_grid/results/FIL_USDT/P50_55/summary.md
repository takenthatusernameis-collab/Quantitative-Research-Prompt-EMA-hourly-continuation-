# EMA Hourly Continuation — FIL/USDT P50_55

**Symbol:** FIL/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 77 |
| net_profit_factor | 0.8557 |
| net_win_rate | 0.5455 |
| gross_profit_factor | 1.1904 |
| gross_win_rate | 0.5455 |
| sharpe_ratio | -0.4006 |
| sortino_ratio | -0.0510 |
| max_drawdown | 0.0816 |
| cagr | -0.0235 |
| net_avg_win | 81.8395 |
| net_avg_loss | -114.7651 |
| avg_hold_time_bars | 6.0519 |
| exposure | 0.0212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
