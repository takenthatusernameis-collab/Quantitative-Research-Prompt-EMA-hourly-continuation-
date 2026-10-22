# EMA Hourly Continuation — XRP/USDT P20_55

**Symbol:** XRP/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 965 |
| net_profit_factor | 0.3271 |
| net_win_rate | 0.4238 |
| gross_profit_factor | 0.8717 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -9.8112 |
| sortino_ratio | -4.3153 |
| max_drawdown | 0.9963 |
| cagr | -0.8919 |
| net_avg_win | 11.8391 |
| net_avg_loss | -26.6273 |
| avg_hold_time_bars | 5.2497 |
| exposure | 0.2303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
