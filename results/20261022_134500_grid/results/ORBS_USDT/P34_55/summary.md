# EMA Hourly Continuation — ORBS/USDT P34_55

**Symbol:** ORBS/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 938 |
| net_profit_factor | 0.3277 |
| net_win_rate | 0.3497 |
| gross_profit_factor | 0.8526 |
| gross_win_rate | 0.3934 |
| sharpe_ratio | -11.9394 |
| sortino_ratio | -5.2579 |
| max_drawdown | 0.9989 |
| cagr | -0.9342 |
| net_avg_win | 14.8420 |
| net_avg_loss | -24.3564 |
| avg_hold_time_bars | 4.2090 |
| exposure | 0.1795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
