# EMA Hourly Continuation — TRAC/USDT P26_34

**Symbol:** TRAC/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.6030 |
| net_win_rate | 0.4633 |
| gross_profit_factor | 0.8562 |
| gross_win_rate | 0.4633 |
| sharpe_ratio | -2.4841 |
| sortino_ratio | -0.5712 |
| max_drawdown | 0.4856 |
| cagr | -0.2303 |
| net_avg_win | 60.9649 |
| net_avg_loss | -87.2871 |
| avg_hold_time_bars | 7.0811 |
| exposure | 0.0834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
