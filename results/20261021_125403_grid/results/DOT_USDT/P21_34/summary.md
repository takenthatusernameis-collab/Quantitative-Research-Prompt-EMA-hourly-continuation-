# EMA Hourly Continuation — DOT/USDT P21_34

**Symbol:** DOT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.6499 |
| net_win_rate | 0.4852 |
| gross_profit_factor | 0.9526 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -2.2242 |
| sortino_ratio | -0.5248 |
| max_drawdown | 0.4789 |
| cagr | -0.2119 |
| net_avg_win | 63.7778 |
| net_avg_loss | -92.4890 |
| avg_hold_time_bars | 5.2593 |
| exposure | 0.0645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
