# EMA Hourly Continuation — CWEB/USDT P8_55

**Symbol:** CWEB/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 770 |
| net_profit_factor | 0.4846 |
| net_win_rate | 0.4052 |
| gross_profit_factor | 0.8653 |
| gross_win_rate | 0.4130 |
| sharpe_ratio | -8.0722 |
| sortino_ratio | -3.1278 |
| max_drawdown | 0.9837 |
| cagr | -0.8024 |
| net_avg_win | 29.6258 |
| net_avg_loss | -41.6436 |
| avg_hold_time_bars | 16.6247 |
| exposure | 0.5819 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
