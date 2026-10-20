# EMA Hourly Continuation — CELO/USDT P34_144

**Symbol:** CELO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7736 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.1141 |
| gross_win_rate | 0.5241 |
| sharpe_ratio | -1.7008 |
| sortino_ratio | -0.5018 |
| max_drawdown | 0.4722 |
| cagr | -0.2113 |
| net_avg_win | 68.4091 |
| net_avg_loss | -94.7466 |
| avg_hold_time_bars | 22.1264 |
| exposure | 0.4355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
