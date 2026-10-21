# EMA Hourly Continuation — TWT/USDT P26_34

**Symbol:** TWT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 229 |
| net_profit_factor | 0.6938 |
| net_win_rate | 0.5415 |
| gross_profit_factor | 1.1597 |
| gross_win_rate | 0.5415 |
| sharpe_ratio | -1.6285 |
| sortino_ratio | -0.3575 |
| max_drawdown | 0.3611 |
| cagr | -0.1494 |
| net_avg_win | 61.0239 |
| net_avg_loss | -103.8762 |
| avg_hold_time_bars | 5.1092 |
| exposure | 0.0532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
