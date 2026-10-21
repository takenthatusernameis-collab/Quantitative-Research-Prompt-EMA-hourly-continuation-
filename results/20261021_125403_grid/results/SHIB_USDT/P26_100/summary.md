# EMA Hourly Continuation — SHIB/USDT P26_100

**Symbol:** SHIB/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.8045 |
| net_win_rate | 0.5090 |
| gross_profit_factor | 1.0591 |
| gross_win_rate | 0.5090 |
| sharpe_ratio | -1.6091 |
| sortino_ratio | -0.4870 |
| max_drawdown | 0.4690 |
| cagr | -0.2008 |
| net_avg_win | 78.3653 |
| net_avg_loss | -100.9834 |
| avg_hold_time_bars | 15.0203 |
| exposure | 0.3031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
