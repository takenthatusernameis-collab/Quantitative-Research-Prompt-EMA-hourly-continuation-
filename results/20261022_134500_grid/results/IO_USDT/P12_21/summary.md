# EMA Hourly Continuation — IO/USDT P12_21

**Symbol:** IO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1408 |
| net_profit_factor | 0.4897 |
| net_win_rate | 0.4318 |
| gross_profit_factor | 0.8794 |
| gross_win_rate | 0.4446 |
| sharpe_ratio | -10.7405 |
| sortino_ratio | -5.8665 |
| max_drawdown | 0.9990 |
| cagr | -0.9468 |
| net_avg_win | 15.7694 |
| net_avg_loss | -24.4723 |
| avg_hold_time_bars | 2.2024 |
| exposure | 0.1501 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
