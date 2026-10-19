# EMA Hourly Continuation — OP/USDT P8_21

**Symbol:** OP/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1631 |
| net_profit_factor | 0.3898 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.9077 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -10.3263 |
| sortino_ratio | -5.8679 |
| max_drawdown | 0.9994 |
| cagr | -0.9473 |
| net_avg_win | 8.6400 |
| net_avg_loss | -18.3619 |
| avg_hold_time_bars | 3.0159 |
| exposure | 0.2236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
