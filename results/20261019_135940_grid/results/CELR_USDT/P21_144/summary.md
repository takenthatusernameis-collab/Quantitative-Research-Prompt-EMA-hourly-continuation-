# EMA Hourly Continuation — CELR/USDT P21_144

**Symbol:** CELR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.6108 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.8863 |
| gross_win_rate | 0.4653 |
| sharpe_ratio | -3.5925 |
| sortino_ratio | -1.1150 |
| max_drawdown | 0.7510 |
| cagr | -0.4107 |
| net_avg_win | 52.3157 |
| net_avg_loss | -70.3632 |
| avg_hold_time_bars | 25.9245 |
| exposure | 0.5748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
