# EMA Hourly Continuation — TAIKO/USDT P20_21

**Symbol:** TAIKO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1119 |
| net_profit_factor | 0.1918 |
| net_win_rate | 0.2779 |
| gross_profit_factor | 0.6295 |
| gross_win_rate | 0.3727 |
| sharpe_ratio | -18.2476 |
| sortino_ratio | -9.6647 |
| max_drawdown | 1.0000 |
| cagr | -0.9960 |
| net_avg_win | 7.6319 |
| net_avg_loss | -15.3137 |
| avg_hold_time_bars | 2.0071 |
| exposure | 0.1079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
