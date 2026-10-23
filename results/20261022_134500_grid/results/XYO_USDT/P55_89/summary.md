# EMA Hourly Continuation — XYO/USDT P55_89

**Symbol:** XYO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 786 |
| net_profit_factor | 0.3636 |
| net_win_rate | 0.3893 |
| gross_profit_factor | 0.7972 |
| gross_win_rate | 0.4211 |
| sharpe_ratio | -9.4947 |
| sortino_ratio | -3.7823 |
| max_drawdown | 0.9924 |
| cagr | -0.8547 |
| net_avg_win | 18.5250 |
| net_avg_loss | -32.4826 |
| avg_hold_time_bars | 4.4733 |
| exposure | 0.1591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
