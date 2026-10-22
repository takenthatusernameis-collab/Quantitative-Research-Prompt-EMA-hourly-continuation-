# EMA Hourly Continuation — STRK/USDT P20_55

**Symbol:** STRK/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 947 |
| net_profit_factor | 0.5849 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9906 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -5.5841 |
| sortino_ratio | -2.4230 |
| max_drawdown | 0.9478 |
| cagr | -0.6876 |
| net_avg_win | 29.7597 |
| net_avg_loss | -45.6795 |
| avg_hold_time_bars | 5.3210 |
| exposure | 0.2290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
