# EMA Hourly Continuation — ROSE/USDT P26_34

**Symbol:** ROSE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1153 |
| net_profit_factor | 0.3334 |
| net_win_rate | 0.4042 |
| gross_profit_factor | 0.8272 |
| gross_win_rate | 0.4337 |
| sharpe_ratio | -11.8326 |
| sortino_ratio | -5.7672 |
| max_drawdown | 0.9994 |
| cagr | -0.9481 |
| net_avg_win | 10.7248 |
| net_avg_loss | -21.8221 |
| avg_hold_time_bars | 2.1275 |
| exposure | 0.1115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
