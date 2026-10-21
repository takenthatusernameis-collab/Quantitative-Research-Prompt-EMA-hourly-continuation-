# EMA Hourly Continuation — ADA/USDT P50_89

**Symbol:** ADA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.6864 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 0.9569 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -1.8557 |
| sortino_ratio | -0.4700 |
| max_drawdown | 0.4268 |
| cagr | -0.1932 |
| net_avg_win | 58.8465 |
| net_avg_loss | -85.1823 |
| avg_hold_time_bars | 7.7556 |
| exposure | 0.1096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
