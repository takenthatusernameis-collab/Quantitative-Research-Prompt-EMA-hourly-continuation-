# EMA Hourly Continuation — IOTX/USDT P12_50

**Symbol:** IOTX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.7892 |
| net_win_rate | 0.5110 |
| gross_profit_factor | 1.0379 |
| gross_win_rate | 0.5110 |
| sharpe_ratio | -1.9064 |
| sortino_ratio | -0.6898 |
| max_drawdown | 0.5903 |
| cagr | -0.2717 |
| net_avg_win | 63.4238 |
| net_avg_loss | -83.9979 |
| avg_hold_time_bars | 11.2934 |
| exposure | 0.3255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
