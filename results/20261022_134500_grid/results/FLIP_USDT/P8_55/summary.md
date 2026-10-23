# EMA Hourly Continuation — FLIP/USDT P8_55

**Symbol:** FLIP/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.5364 |
| net_win_rate | 0.4298 |
| gross_profit_factor | 0.8746 |
| gross_win_rate | 0.4459 |
| sharpe_ratio | -6.0327 |
| sortino_ratio | -2.1980 |
| max_drawdown | 0.9366 |
| cagr | -0.6639 |
| net_avg_win | 36.8109 |
| net_avg_loss | -51.7322 |
| avg_hold_time_bars | 17.7588 |
| exposure | 0.5521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
