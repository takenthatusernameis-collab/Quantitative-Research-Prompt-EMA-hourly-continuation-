# EMA Hourly Continuation — FLOW/USDT P55_200

**Symbol:** FLOW/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.7179 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.8889 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -1.7767 |
| sortino_ratio | -0.4403 |
| max_drawdown | 0.4044 |
| cagr | -0.1835 |
| net_avg_win | 71.0033 |
| net_avg_loss | -88.3907 |
| avg_hold_time_bars | 26.4488 |
| exposure | 0.3643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
