# EMA Hourly Continuation — ADA/USDT P26_50

**Symbol:** ADA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 923 |
| net_profit_factor | 0.3617 |
| net_win_rate | 0.4225 |
| gross_profit_factor | 0.8358 |
| gross_win_rate | 0.4453 |
| sharpe_ratio | -9.0880 |
| sortino_ratio | -3.9143 |
| max_drawdown | 0.9929 |
| cagr | -0.8596 |
| net_avg_win | 14.4230 |
| net_avg_loss | -29.1796 |
| avg_hold_time_bars | 3.7064 |
| exposure | 0.1555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
