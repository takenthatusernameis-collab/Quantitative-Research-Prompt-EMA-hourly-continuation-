# EMA Hourly Continuation — ANYONE/USDT P55_200

**Symbol:** ANYONE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.6693 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8502 |
| gross_win_rate | 0.4653 |
| sharpe_ratio | -2.3109 |
| sortino_ratio | -0.6277 |
| max_drawdown | 0.5009 |
| cagr | -0.2533 |
| net_avg_win | 63.9059 |
| net_avg_loss | -82.0719 |
| avg_hold_time_bars | 22.9124 |
| exposure | 0.3832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
