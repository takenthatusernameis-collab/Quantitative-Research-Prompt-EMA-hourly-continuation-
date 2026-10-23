# EMA Hourly Continuation — ZKJ/USDT P12_20

**Symbol:** ZKJ/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1632 |
| net_profit_factor | 0.1810 |
| net_win_rate | 0.2463 |
| gross_profit_factor | 0.5120 |
| gross_win_rate | 0.3438 |
| sharpe_ratio | -22.2919 |
| sortino_ratio | -13.7243 |
| max_drawdown | 1.0000 |
| cagr | -0.9995 |
| net_avg_win | 5.4975 |
| net_avg_loss | -9.9268 |
| avg_hold_time_bars | 2.7347 |
| exposure | 0.2029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
