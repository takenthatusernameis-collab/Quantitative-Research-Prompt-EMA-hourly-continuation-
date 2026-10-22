# EMA Hourly Continuation — MTL/USDT P12_26

**Symbol:** MTL/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.5065 |
| net_win_rate | 0.4431 |
| gross_profit_factor | 0.8150 |
| gross_win_rate | 0.4461 |
| sharpe_ratio | -5.9827 |
| sortino_ratio | -2.2384 |
| max_drawdown | 0.9309 |
| cagr | -0.6498 |
| net_avg_win | 31.3694 |
| net_avg_loss | -49.2862 |
| avg_hold_time_bars | 5.6283 |
| exposure | 0.1747 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
