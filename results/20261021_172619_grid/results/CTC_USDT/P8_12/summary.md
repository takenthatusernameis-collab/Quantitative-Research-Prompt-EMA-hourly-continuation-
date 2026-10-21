# EMA Hourly Continuation — CTC/USDT P8_12

**Symbol:** CTC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.5737 |
| net_win_rate | 0.4725 |
| gross_profit_factor | 0.8834 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -3.0234 |
| sortino_ratio | -0.8049 |
| max_drawdown | 0.6167 |
| cagr | -0.3083 |
| net_avg_win | 49.8438 |
| net_avg_loss | -77.8143 |
| avg_hold_time_bars | 5.5507 |
| exposure | 0.0870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
