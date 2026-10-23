# EMA Hourly Continuation — ALT/USDT P89_200

**Symbol:** ALT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.6516 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.9141 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -2.5561 |
| sortino_ratio | -0.6953 |
| max_drawdown | 0.5647 |
| cagr | -0.2745 |
| net_avg_win | 60.5140 |
| net_avg_loss | -81.4367 |
| avg_hold_time_bars | 13.2705 |
| exposure | 0.2208 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
