# EMA Hourly Continuation — ZBCN/USDT P34_144

**Symbol:** ZBCN/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.8609 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 1.0027 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -0.9110 |
| sortino_ratio | -0.2577 |
| max_drawdown | 0.3890 |
| cagr | -0.1145 |
| net_avg_win | 83.1064 |
| net_avg_loss | -97.5459 |
| avg_hold_time_bars | 17.8099 |
| exposure | 0.3164 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
