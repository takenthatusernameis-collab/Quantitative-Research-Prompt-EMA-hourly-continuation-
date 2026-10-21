# EMA Hourly Continuation — IO/USDT P34_50

**Symbol:** IO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 205 |
| net_profit_factor | 0.7574 |
| net_win_rate | 0.4927 |
| gross_profit_factor | 0.9733 |
| gross_win_rate | 0.4927 |
| sharpe_ratio | -1.2960 |
| sortino_ratio | -0.2743 |
| max_drawdown | 0.2820 |
| cagr | -0.1181 |
| net_avg_win | 79.2599 |
| net_avg_loss | -101.6346 |
| avg_hold_time_bars | 5.2293 |
| exposure | 0.0519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
