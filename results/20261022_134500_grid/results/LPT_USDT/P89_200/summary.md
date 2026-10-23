# EMA Hourly Continuation — LPT/USDT P89_200

**Symbol:** LPT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.6196 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.9683 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -3.1231 |
| sortino_ratio | -0.8852 |
| max_drawdown | 0.6703 |
| cagr | -0.3461 |
| net_avg_win | 55.6428 |
| net_avg_loss | -80.1969 |
| avg_hold_time_bars | 10.7912 |
| exposure | 0.1996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
