# EMA Hourly Continuation — CVX/USDT P26_34

**Symbol:** CVX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 0.6134 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.8902 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -2.2528 |
| sortino_ratio | -0.5073 |
| max_drawdown | 0.4708 |
| cagr | -0.2079 |
| net_avg_win | 59.5839 |
| net_avg_loss | -88.8550 |
| avg_hold_time_bars | 4.5911 |
| exposure | 0.0515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
