# EMA Hourly Continuation — CSPR/USDT P20_21

**Symbol:** CSPR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 141 |
| net_profit_factor | 0.6100 |
| net_win_rate | 0.4468 |
| gross_profit_factor | 0.8228 |
| gross_win_rate | 0.4468 |
| sharpe_ratio | -1.8779 |
| sortino_ratio | -0.3175 |
| max_drawdown | 0.3150 |
| cagr | -0.1352 |
| net_avg_win | 75.8884 |
| net_avg_loss | -100.4833 |
| avg_hold_time_bars | 6.0496 |
| exposure | 0.0388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
