# EMA Hourly Continuation — GMT/USDT P8_26

**Symbol:** GMT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.6766 |
| net_win_rate | 0.4946 |
| gross_profit_factor | 0.9233 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -2.6167 |
| sortino_ratio | -0.9517 |
| max_drawdown | 0.6814 |
| cagr | -0.3531 |
| net_avg_win | 43.7528 |
| net_avg_loss | -63.2759 |
| avg_hold_time_bars | 7.0607 |
| exposure | 0.2064 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
