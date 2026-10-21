# EMA Hourly Continuation — BRETT/USDT P8_26

**Symbol:** BRETT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.8555 |
| net_win_rate | 0.5142 |
| gross_profit_factor | 1.0515 |
| gross_win_rate | 0.5142 |
| sharpe_ratio | -1.2558 |
| sortino_ratio | -0.4684 |
| max_drawdown | 0.4745 |
| cagr | -0.1971 |
| net_avg_win | 73.4987 |
| net_avg_loss | -90.9172 |
| avg_hold_time_bars | 7.0959 |
| exposure | 0.2171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
