# EMA Hourly Continuation — UQC/USDT P8_144

**Symbol:** UQC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 200 |
| net_profit_factor | 0.3635 |
| net_win_rate | 0.3050 |
| gross_profit_factor | 0.4633 |
| gross_win_rate | 0.3050 |
| sharpe_ratio | -4.5019 |
| sortino_ratio | -0.8840 |
| max_drawdown | 0.6592 |
| cagr | -0.3454 |
| net_avg_win | 61.4708 |
| net_avg_loss | -74.2063 |
| avg_hold_time_bars | 86.3300 |
| exposure | 0.7814 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
