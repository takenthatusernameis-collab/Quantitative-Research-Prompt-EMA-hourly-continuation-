# EMA Hourly Continuation — STRK/USDT P50_89

**Symbol:** STRK/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 0.7716 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9859 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.4868 |
| sortino_ratio | -0.3882 |
| max_drawdown | 0.4010 |
| cagr | -0.1636 |
| net_avg_win | 74.0047 |
| net_avg_loss | -94.7603 |
| avg_hold_time_bars | 6.5241 |
| exposure | 0.0985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
