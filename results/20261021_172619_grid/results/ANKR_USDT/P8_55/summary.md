# EMA Hourly Continuation — ANKR/USDT P8_55

**Symbol:** ANKR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.7214 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.9456 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -3.0326 |
| sortino_ratio | -1.1201 |
| max_drawdown | 0.7425 |
| cagr | -0.4030 |
| net_avg_win | 58.5759 |
| net_avg_loss | -74.6863 |
| avg_hold_time_bars | 16.7925 |
| exposure | 0.5114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
