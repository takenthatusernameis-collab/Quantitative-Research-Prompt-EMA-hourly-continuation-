# EMA Hourly Continuation — HTX/USDT P26_34

**Symbol:** HTX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.2754 |
| net_win_rate | 0.3043 |
| gross_profit_factor | 0.5341 |
| gross_win_rate | 0.3106 |
| sharpe_ratio | -7.6199 |
| sortino_ratio | -2.0266 |
| max_drawdown | 0.9147 |
| cagr | -0.6231 |
| net_avg_win | 35.4829 |
| net_avg_loss | -56.3583 |
| avg_hold_time_bars | 5.4193 |
| exposure | 0.0790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
