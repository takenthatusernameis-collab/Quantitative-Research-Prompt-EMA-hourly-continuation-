# EMA Hourly Continuation — BOSON/USDT P21_50

**Symbol:** BOSON/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 907 |
| net_profit_factor | 0.5601 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.8970 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -5.7629 |
| sortino_ratio | -2.4353 |
| max_drawdown | 0.9478 |
| cagr | -0.6902 |
| net_avg_win | 29.3478 |
| net_avg_loss | -43.4171 |
| avg_hold_time_bars | 5.7111 |
| exposure | 0.2355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
