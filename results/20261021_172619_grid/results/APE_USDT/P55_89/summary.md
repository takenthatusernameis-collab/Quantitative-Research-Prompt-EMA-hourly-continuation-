# EMA Hourly Continuation — APE/USDT P55_89

**Symbol:** APE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6704 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.9068 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -2.3171 |
| sortino_ratio | -0.6073 |
| max_drawdown | 0.5182 |
| cagr | -0.2428 |
| net_avg_win | 63.8888 |
| net_avg_loss | -86.6407 |
| avg_hold_time_bars | 5.8452 |
| exposure | 0.0893 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
