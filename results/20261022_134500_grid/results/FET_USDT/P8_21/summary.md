# EMA Hourly Continuation — FET/USDT P8_21

**Symbol:** FET/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1754 |
| net_profit_factor | 0.4334 |
| net_win_rate | 0.4339 |
| gross_profit_factor | 0.8065 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -11.3625 |
| sortino_ratio | -6.6855 |
| max_drawdown | 0.9998 |
| cagr | -0.9655 |
| net_avg_win | 10.0512 |
| net_avg_loss | -17.7712 |
| avg_hold_time_bars | 2.6112 |
| exposure | 0.2082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
