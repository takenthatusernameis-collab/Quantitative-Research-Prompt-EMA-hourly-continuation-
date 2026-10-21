# EMA Hourly Continuation — BNB/USDT P20_55

**Symbol:** BNB/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.5835 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 1.0196 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -3.8245 |
| sortino_ratio | -1.2107 |
| max_drawdown | 0.7600 |
| cagr | -0.4260 |
| net_avg_win | 43.8996 |
| net_avg_loss | -74.9170 |
| avg_hold_time_bars | 8.1518 |
| exposure | 0.1782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
