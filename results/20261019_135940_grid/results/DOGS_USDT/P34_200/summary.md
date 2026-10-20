# EMA Hourly Continuation — DOGS/USDT P34_200

**Symbol:** DOGS/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.6611 |
| net_win_rate | 0.4794 |
| gross_profit_factor | 0.9236 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -2.7245 |
| sortino_ratio | -0.7580 |
| max_drawdown | 0.5804 |
| cagr | -0.3073 |
| net_avg_win | 65.3728 |
| net_avg_loss | -91.0576 |
| avg_hold_time_bars | 28.0853 |
| exposure | 0.5066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
