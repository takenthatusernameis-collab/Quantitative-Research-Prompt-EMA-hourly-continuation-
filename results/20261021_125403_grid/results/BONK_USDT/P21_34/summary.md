# EMA Hourly Continuation — BONK/USDT P21_34

**Symbol:** BONK/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.7832 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 1.0037 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -1.1750 |
| sortino_ratio | -0.2666 |
| max_drawdown | 0.3556 |
| cagr | -0.1162 |
| net_avg_win | 76.4964 |
| net_avg_loss | -99.2431 |
| avg_hold_time_bars | 5.7920 |
| exposure | 0.0658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
