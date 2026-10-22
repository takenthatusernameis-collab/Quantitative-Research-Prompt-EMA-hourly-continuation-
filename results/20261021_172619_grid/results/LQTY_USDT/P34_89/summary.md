# EMA Hourly Continuation — LQTY/USDT P34_89

**Symbol:** LQTY/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.6783 |
| net_win_rate | 0.4644 |
| gross_profit_factor | 0.8831 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -2.8314 |
| sortino_ratio | -0.8796 |
| max_drawdown | 0.6407 |
| cagr | -0.3319 |
| net_avg_win | 60.6385 |
| net_avg_loss | -77.5251 |
| avg_hold_time_bars | 10.9017 |
| exposure | 0.2358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
