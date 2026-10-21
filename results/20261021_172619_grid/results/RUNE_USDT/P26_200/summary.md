# EMA Hourly Continuation — RUNE/USDT P26_200

**Symbol:** RUNE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.8691 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 1.0441 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -0.6178 |
| sortino_ratio | -0.1374 |
| max_drawdown | 0.2079 |
| cagr | -0.0631 |
| net_avg_win | 81.5846 |
| net_avg_loss | -98.6821 |
| avg_hold_time_bars | 59.3292 |
| exposure | 0.6472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
