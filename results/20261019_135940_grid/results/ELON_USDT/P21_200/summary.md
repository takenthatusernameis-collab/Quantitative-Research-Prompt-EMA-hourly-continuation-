# EMA Hourly Continuation — ELON/USDT P21_200

**Symbol:** ELON/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.5524 |
| net_win_rate | 0.4256 |
| gross_profit_factor | 0.7631 |
| gross_win_rate | 0.4277 |
| sharpe_ratio | -4.1947 |
| sortino_ratio | -1.2909 |
| max_drawdown | 0.7854 |
| cagr | -0.4547 |
| net_avg_win | 47.5439 |
| net_avg_loss | -63.7629 |
| avg_hold_time_bars | 25.5975 |
| exposure | 0.5550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
