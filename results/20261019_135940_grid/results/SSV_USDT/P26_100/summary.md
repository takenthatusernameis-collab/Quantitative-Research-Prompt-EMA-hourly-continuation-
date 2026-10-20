# EMA Hourly Continuation — SSV/USDT P26_100

**Symbol:** SSV/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 694 |
| net_profit_factor | 0.5894 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.8846 |
| gross_win_rate | 0.4755 |
| sharpe_ratio | -4.4179 |
| sortino_ratio | -1.6347 |
| max_drawdown | 0.8682 |
| cagr | -0.5428 |
| net_avg_win | 38.3820 |
| net_avg_loss | -56.3724 |
| avg_hold_time_bars | 11.3919 |
| exposure | 0.3578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
