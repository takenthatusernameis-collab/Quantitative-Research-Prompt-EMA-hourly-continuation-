# EMA Hourly Continuation — ZK/USDT P20_89

**Symbol:** ZK/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.8022 |
| net_win_rate | 0.4919 |
| gross_profit_factor | 0.9792 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -1.6955 |
| sortino_ratio | -0.5587 |
| max_drawdown | 0.4894 |
| cagr | -0.2281 |
| net_avg_win | 75.5607 |
| net_avg_loss | -91.2010 |
| avg_hold_time_bars | 15.4516 |
| exposure | 0.3737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
