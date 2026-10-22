# EMA Hourly Continuation — AERO/USDT P8_20

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1635 |
| net_profit_factor | 0.3456 |
| net_win_rate | 0.4275 |
| gross_profit_factor | 0.6842 |
| gross_win_rate | 0.4477 |
| sharpe_ratio | -11.2166 |
| sortino_ratio | -6.3707 |
| max_drawdown | 0.9997 |
| cagr | -0.9597 |
| net_avg_win | 7.5516 |
| net_avg_loss | -16.3199 |
| avg_hold_time_bars | 2.8532 |
| exposure | 0.2120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
