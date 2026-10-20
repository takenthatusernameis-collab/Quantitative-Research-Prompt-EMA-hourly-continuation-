# EMA Hourly Continuation — REQ/USDT P21_34

**Symbol:** REQ/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1250 |
| net_profit_factor | 0.3204 |
| net_win_rate | 0.3608 |
| gross_profit_factor | 0.8703 |
| gross_win_rate | 0.4248 |
| sharpe_ratio | -14.4335 |
| sortino_ratio | -7.4422 |
| max_drawdown | 0.9999 |
| cagr | -0.9790 |
| net_avg_win | 10.4537 |
| net_avg_loss | -18.4155 |
| avg_hold_time_bars | 3.1368 |
| exposure | 0.1782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
