# EMA Hourly Continuation — CSPR/USDT P20_55

**Symbol:** CSPR/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.6791 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.8757 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -2.7583 |
| sortino_ratio | -0.8758 |
| max_drawdown | 0.6398 |
| cagr | -0.3309 |
| net_avg_win | 58.2018 |
| net_avg_loss | -74.4319 |
| avg_hold_time_bars | 7.5171 |
| exposure | 0.1698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
