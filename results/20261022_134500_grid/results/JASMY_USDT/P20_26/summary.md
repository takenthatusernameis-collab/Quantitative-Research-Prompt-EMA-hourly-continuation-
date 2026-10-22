# EMA Hourly Continuation — JASMY/USDT P20_26

**Symbol:** JASMY/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1198 |
| net_profit_factor | 0.2662 |
| net_win_rate | 0.3756 |
| gross_profit_factor | 0.6759 |
| gross_win_rate | 0.4132 |
| sharpe_ratio | -13.8025 |
| sortino_ratio | -6.9290 |
| max_drawdown | 0.9999 |
| cagr | -0.9748 |
| net_avg_win | 8.0608 |
| net_avg_loss | -18.2171 |
| avg_hold_time_bars | 1.6987 |
| exposure | 0.0925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
