# EMA Hourly Continuation — BOME/USDT P89_200

**Symbol:** BOME/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.8068 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 0.9661 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -0.9738 |
| sortino_ratio | -0.2286 |
| max_drawdown | 0.2719 |
| cagr | -0.1008 |
| net_avg_win | 73.0293 |
| net_avg_loss | -89.8437 |
| avg_hold_time_bars | 16.3011 |
| exposure | 0.1993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
