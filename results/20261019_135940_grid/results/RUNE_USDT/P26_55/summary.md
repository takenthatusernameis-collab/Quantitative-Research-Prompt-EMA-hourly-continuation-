# EMA Hourly Continuation — RUNE/USDT P26_55

**Symbol:** RUNE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 880 |
| net_profit_factor | 0.5136 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9619 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -6.1735 |
| sortino_ratio | -2.5771 |
| max_drawdown | 0.9584 |
| cagr | -0.7176 |
| net_avg_win | 23.9229 |
| net_avg_loss | -43.1109 |
| avg_hold_time_bars | 4.6375 |
| exposure | 0.1855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
