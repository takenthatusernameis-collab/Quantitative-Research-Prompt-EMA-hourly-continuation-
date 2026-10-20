# EMA Hourly Continuation — DODO/USDT P100_144

**Symbol:** DODO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.4252 |
| net_win_rate | 0.4198 |
| gross_profit_factor | 0.7845 |
| gross_win_rate | 0.4317 |
| sharpe_ratio | -6.4961 |
| sortino_ratio | -2.2169 |
| max_drawdown | 0.9361 |
| cagr | -0.6600 |
| net_avg_win | 28.0886 |
| net_avg_loss | -47.7994 |
| avg_hold_time_bars | 4.0870 |
| exposure | 0.1084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
