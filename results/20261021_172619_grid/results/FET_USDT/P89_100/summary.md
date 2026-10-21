# EMA Hourly Continuation — FET/USDT P89_100

**Symbol:** FET/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 76 |
| net_profit_factor | 0.7272 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9466 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -0.8627 |
| sortino_ratio | -0.1077 |
| max_drawdown | 0.1447 |
| cagr | -0.0483 |
| net_avg_win | 84.2154 |
| net_avg_loss | -109.8633 |
| avg_hold_time_bars | 7.4474 |
| exposure | 0.0257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
