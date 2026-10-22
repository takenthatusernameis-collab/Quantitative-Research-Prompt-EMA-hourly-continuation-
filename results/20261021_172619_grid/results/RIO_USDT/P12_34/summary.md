# EMA Hourly Continuation — RIO/USDT P12_34

**Symbol:** RIO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.7885 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.9310 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -1.8737 |
| sortino_ratio | -0.6228 |
| max_drawdown | 0.5238 |
| cagr | -0.2508 |
| net_avg_win | 74.0330 |
| net_avg_loss | -86.2024 |
| avg_hold_time_bars | 7.1763 |
| exposure | 0.1776 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
