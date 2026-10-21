# EMA Hourly Continuation — TRAC/USDT P21_26

**Symbol:** TRAC/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.7434 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0521 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -1.4971 |
| sortino_ratio | -0.3318 |
| max_drawdown | 0.3664 |
| cagr | -0.1413 |
| net_avg_win | 76.1189 |
| net_avg_loss | -105.8956 |
| avg_hold_time_bars | 8.4706 |
| exposure | 0.0916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
