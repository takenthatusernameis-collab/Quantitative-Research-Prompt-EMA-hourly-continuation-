# EMA Hourly Continuation — ENS/USDT P55_100

**Symbol:** ENS/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.4781 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.8375 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -5.8522 |
| sortino_ratio | -2.0745 |
| max_drawdown | 0.9253 |
| cagr | -0.6405 |
| net_avg_win | 29.7897 |
| net_avg_loss | -50.4110 |
| avg_hold_time_bars | 5.5150 |
| exposure | 0.1592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
