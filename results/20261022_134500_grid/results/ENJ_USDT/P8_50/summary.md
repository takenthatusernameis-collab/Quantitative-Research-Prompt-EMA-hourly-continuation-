# EMA Hourly Continuation — ENJ/USDT P8_50

**Symbol:** ENJ/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1137 |
| net_profit_factor | 0.6007 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.9702 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -5.9992 |
| sortino_ratio | -2.8425 |
| max_drawdown | 0.9690 |
| cagr | -0.7458 |
| net_avg_win | 27.0257 |
| net_avg_loss | -40.5535 |
| avg_hold_time_bars | 8.7898 |
| exposure | 0.4522 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
