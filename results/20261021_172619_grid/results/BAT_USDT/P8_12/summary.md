# EMA Hourly Continuation — BAT/USDT P8_12

**Symbol:** BAT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.5908 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 0.9934 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -3.4267 |
| sortino_ratio | -1.0735 |
| max_drawdown | 0.7180 |
| cagr | -0.3883 |
| net_avg_win | 43.3746 |
| net_avg_loss | -73.1038 |
| avg_hold_time_bars | 4.2262 |
| exposure | 0.0909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
