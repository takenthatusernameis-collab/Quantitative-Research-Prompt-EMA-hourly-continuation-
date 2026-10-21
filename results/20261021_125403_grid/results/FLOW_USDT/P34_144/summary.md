# EMA Hourly Continuation — FLOW/USDT P34_144

**Symbol:** FLOW/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7501 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9236 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -1.7401 |
| sortino_ratio | -0.4635 |
| max_drawdown | 0.4299 |
| cagr | -0.1930 |
| net_avg_win | 74.4069 |
| net_avg_loss | -91.5644 |
| avg_hold_time_bars | 28.0514 |
| exposure | 0.4463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
