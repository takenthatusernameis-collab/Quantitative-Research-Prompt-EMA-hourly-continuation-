# EMA Hourly Continuation — AERO/USDT P8_20

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.8349 |
| net_win_rate | 0.5285 |
| gross_profit_factor | 1.0990 |
| gross_win_rate | 0.5285 |
| sharpe_ratio | -1.1773 |
| sortino_ratio | -0.3828 |
| max_drawdown | 0.4465 |
| cagr | -0.1631 |
| net_avg_win | 67.7693 |
| net_avg_loss | -90.9794 |
| avg_hold_time_bars | 5.4578 |
| exposure | 0.1263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
