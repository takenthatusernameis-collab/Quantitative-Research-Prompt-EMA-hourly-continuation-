# EMA Hourly Continuation — CHR/USDT P21_55

**Symbol:** CHR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 961 |
| net_profit_factor | 0.5232 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.8848 |
| gross_win_rate | 0.4568 |
| sharpe_ratio | -6.5014 |
| sortino_ratio | -2.8389 |
| max_drawdown | 0.9686 |
| cagr | -0.7431 |
| net_avg_win | 25.0455 |
| net_avg_loss | -37.7933 |
| avg_hold_time_bars | 5.5765 |
| exposure | 0.2425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
