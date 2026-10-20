# EMA Hourly Continuation — ZEN/USDT P21_50

**Symbol:** ZEN/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1046 |
| net_profit_factor | 0.4739 |
| net_win_rate | 0.4484 |
| gross_profit_factor | 0.8610 |
| gross_win_rate | 0.4656 |
| sharpe_ratio | -7.4286 |
| sortino_ratio | -3.3682 |
| max_drawdown | 0.9855 |
| cagr | -0.8116 |
| net_avg_win | 18.9149 |
| net_avg_loss | -32.4436 |
| avg_hold_time_bars | 4.3891 |
| exposure | 0.2087 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
