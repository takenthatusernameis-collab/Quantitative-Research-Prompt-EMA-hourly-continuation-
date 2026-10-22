# EMA Hourly Continuation — MTL/USDT P8_100

**Symbol:** MTL/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.7418 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9715 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -2.3069 |
| sortino_ratio | -0.6785 |
| max_drawdown | 0.5956 |
| cagr | -0.2698 |
| net_avg_win | 76.3484 |
| net_avg_loss | -95.5104 |
| avg_hold_time_bars | 37.9556 |
| exposure | 0.7351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
