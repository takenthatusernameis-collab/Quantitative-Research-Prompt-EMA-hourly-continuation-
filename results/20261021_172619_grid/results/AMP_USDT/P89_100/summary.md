# EMA Hourly Continuation — AMP/USDT P89_100

**Symbol:** AMP/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 133 |
| net_profit_factor | 0.4423 |
| net_win_rate | 0.4060 |
| gross_profit_factor | 0.6523 |
| gross_win_rate | 0.4060 |
| sharpe_ratio | -2.7144 |
| sortino_ratio | -0.4472 |
| max_drawdown | 0.4447 |
| cagr | -0.1875 |
| net_avg_win | 59.6760 |
| net_avg_loss | -92.2152 |
| avg_hold_time_bars | 6.0526 |
| exposure | 0.0366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
