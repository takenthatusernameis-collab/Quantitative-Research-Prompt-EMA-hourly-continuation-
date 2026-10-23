# EMA Hourly Continuation — TNSR/USDT P8_26

**Symbol:** TNSR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1515 |
| net_profit_factor | 0.6440 |
| net_win_rate | 0.4561 |
| gross_profit_factor | 1.0293 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -7.9907 |
| sortino_ratio | -4.3818 |
| max_drawdown | 0.9952 |
| cagr | -0.8785 |
| net_avg_win | 26.0493 |
| net_avg_loss | -33.9211 |
| avg_hold_time_bars | 3.9413 |
| exposure | 0.2702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
