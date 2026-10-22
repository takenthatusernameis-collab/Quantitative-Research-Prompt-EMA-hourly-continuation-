# EMA Hourly Continuation — BAND/USDT P12_55

**Symbol:** BAND/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.7978 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0507 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -2.1388 |
| sortino_ratio | -0.7818 |
| max_drawdown | 0.6516 |
| cagr | -0.3021 |
| net_avg_win | 71.3252 |
| net_avg_loss | -91.0547 |
| avg_hold_time_bars | 13.3135 |
| exposure | 0.3940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
