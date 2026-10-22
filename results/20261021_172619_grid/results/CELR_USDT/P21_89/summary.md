# EMA Hourly Continuation — CELR/USDT P21_89

**Symbol:** CELR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.7283 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 0.9263 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -2.5160 |
| sortino_ratio | -0.8510 |
| max_drawdown | 0.6495 |
| cagr | -0.3242 |
| net_avg_win | 62.3241 |
| net_avg_loss | -78.3247 |
| avg_hold_time_bars | 15.0566 |
| exposure | 0.3849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
