# EMA Hourly Continuation — XYO/USDT P100_200

**Symbol:** XYO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.4687 |
| net_win_rate | 0.4239 |
| gross_profit_factor | 0.7709 |
| gross_win_rate | 0.4280 |
| sharpe_ratio | -5.4564 |
| sortino_ratio | -1.7009 |
| max_drawdown | 0.8790 |
| cagr | -0.5659 |
| net_avg_win | 37.0704 |
| net_avg_loss | -58.2021 |
| avg_hold_time_bars | 8.8316 |
| exposure | 0.1970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
