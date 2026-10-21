# EMA Hourly Continuation — REZ/USDT P8_200

**Symbol:** REZ/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.8917 |
| net_win_rate | 0.5087 |
| gross_profit_factor | 1.0233 |
| gross_win_rate | 0.5087 |
| sharpe_ratio | -0.6260 |
| sortino_ratio | -0.1681 |
| max_drawdown | 0.2598 |
| cagr | -0.0781 |
| net_avg_win | 85.2170 |
| net_avg_loss | -98.9393 |
| avg_hold_time_bars | 47.8555 |
| exposure | 0.7639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
