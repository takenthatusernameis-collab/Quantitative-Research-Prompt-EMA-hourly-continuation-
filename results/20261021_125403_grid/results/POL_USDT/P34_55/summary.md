# EMA Hourly Continuation — POL/USDT P34_55

**Symbol:** POL/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.5631 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.7987 |
| gross_win_rate | 0.4548 |
| sharpe_ratio | -2.8576 |
| sortino_ratio | -0.7060 |
| max_drawdown | 0.5606 |
| cagr | -0.2770 |
| net_avg_win | 52.8036 |
| net_avg_loss | -78.2396 |
| avg_hold_time_bars | 6.7893 |
| exposure | 0.0923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
