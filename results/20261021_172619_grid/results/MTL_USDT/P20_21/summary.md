# EMA Hourly Continuation — MTL/USDT P20_21

**Symbol:** MTL/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.4541 |
| net_win_rate | 0.4603 |
| gross_profit_factor | 0.8520 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -4.2189 |
| sortino_ratio | -1.0740 |
| max_drawdown | 0.7303 |
| cagr | -0.3962 |
| net_avg_win | 41.2935 |
| net_avg_loss | -77.5664 |
| avg_hold_time_bars | 4.9460 |
| exposure | 0.0705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
