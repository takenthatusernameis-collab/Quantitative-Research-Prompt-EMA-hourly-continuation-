# EMA Hourly Continuation — COMP/USDT P20_55

**Symbol:** COMP/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 603 |
| net_profit_factor | 0.6723 |
| net_win_rate | 0.5058 |
| gross_profit_factor | 0.9561 |
| gross_win_rate | 0.5058 |
| sharpe_ratio | -2.6456 |
| sortino_ratio | -0.9323 |
| max_drawdown | 0.7019 |
| cagr | -0.3479 |
| net_avg_win | 44.2720 |
| net_avg_loss | -67.4029 |
| avg_hold_time_bars | 8.8458 |
| exposure | 0.2425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
