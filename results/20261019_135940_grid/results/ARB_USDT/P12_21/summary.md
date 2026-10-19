# EMA Hourly Continuation — ARB/USDT P12_21

**Symbol:** ARB/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1433 |
| net_profit_factor | 0.2641 |
| net_win_rate | 0.4278 |
| gross_profit_factor | 0.8389 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -11.9879 |
| sortino_ratio | -6.4313 |
| max_drawdown | 0.9998 |
| cagr | -0.9628 |
| net_avg_win | 5.8519 |
| net_avg_loss | -16.5667 |
| avg_hold_time_bars | 2.1089 |
| exposure | 0.1374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
