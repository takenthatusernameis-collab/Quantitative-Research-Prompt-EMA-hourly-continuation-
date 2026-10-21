# EMA Hourly Continuation — UMA/USDT P144_200

**Symbol:** UMA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 237 |
| net_profit_factor | 0.4906 |
| net_win_rate | 0.4093 |
| gross_profit_factor | 0.7006 |
| gross_win_rate | 0.4093 |
| sharpe_ratio | -3.4958 |
| sortino_ratio | -0.7665 |
| max_drawdown | 0.5934 |
| cagr | -0.2987 |
| net_avg_win | 58.5568 |
| net_avg_loss | -82.6997 |
| avg_hold_time_bars | 7.9578 |
| exposure | 0.0857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
