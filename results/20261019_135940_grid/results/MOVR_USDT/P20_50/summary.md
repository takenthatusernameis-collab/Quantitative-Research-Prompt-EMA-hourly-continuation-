# EMA Hourly Continuation — MOVR/USDT P20_50

**Symbol:** MOVR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1015 |
| net_profit_factor | 0.4163 |
| net_win_rate | 0.4246 |
| gross_profit_factor | 0.7673 |
| gross_win_rate | 0.4394 |
| sharpe_ratio | -7.9506 |
| sortino_ratio | -3.5532 |
| max_drawdown | 0.9880 |
| cagr | -0.8269 |
| net_avg_win | 16.3458 |
| net_avg_loss | -28.9773 |
| avg_hold_time_bars | 4.9596 |
| exposure | 0.2288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
