# EMA Hourly Continuation — XYO/USDT P21_55

**Symbol:** XYO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1071 |
| net_profit_factor | 0.4199 |
| net_win_rate | 0.3978 |
| gross_profit_factor | 0.7735 |
| gross_win_rate | 0.4146 |
| sharpe_ratio | -9.9773 |
| sortino_ratio | -4.6256 |
| max_drawdown | 0.9969 |
| cagr | -0.8990 |
| net_avg_win | 16.9401 |
| net_avg_loss | -26.6445 |
| avg_hold_time_bars | 5.1027 |
| exposure | 0.2473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
