# EMA Hourly Continuation — ZEN/USDT P50_100

**Symbol:** ZEN/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.5610 |
| net_win_rate | 0.4592 |
| gross_profit_factor | 0.9504 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -5.0422 |
| sortino_ratio | -1.8293 |
| max_drawdown | 0.8934 |
| cagr | -0.5865 |
| net_avg_win | 37.4658 |
| net_avg_loss | -56.7076 |
| avg_hold_time_bars | 6.0378 |
| exposure | 0.1817 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
