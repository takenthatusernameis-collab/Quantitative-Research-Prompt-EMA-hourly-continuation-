# EMA Hourly Continuation — KAS/USDT P8_50

**Symbol:** KAS/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1166 |
| net_profit_factor | 0.5632 |
| net_win_rate | 0.4957 |
| gross_profit_factor | 0.9900 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -5.5873 |
| sortino_ratio | -2.6607 |
| max_drawdown | 0.9652 |
| cagr | -0.7325 |
| net_avg_win | 21.4980 |
| net_avg_loss | -37.5188 |
| avg_hold_time_bars | 8.5978 |
| exposure | 0.4557 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
