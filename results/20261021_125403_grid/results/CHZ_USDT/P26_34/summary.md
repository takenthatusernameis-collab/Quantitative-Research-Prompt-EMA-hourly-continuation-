# EMA Hourly Continuation — CHZ/USDT P26_34

**Symbol:** CHZ/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 189 |
| net_profit_factor | 0.4631 |
| net_win_rate | 0.3915 |
| gross_profit_factor | 0.6532 |
| gross_win_rate | 0.3915 |
| sharpe_ratio | -3.3019 |
| sortino_ratio | -0.6462 |
| max_drawdown | 0.5387 |
| cagr | -0.2589 |
| net_avg_win | 61.6201 |
| net_avg_loss | -85.6271 |
| avg_hold_time_bars | 4.4550 |
| exposure | 0.0383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
