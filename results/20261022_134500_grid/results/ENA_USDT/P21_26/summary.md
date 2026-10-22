# EMA Hourly Continuation — ENA/USDT P21_26

**Symbol:** ENA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1194 |
| net_profit_factor | 0.3322 |
| net_win_rate | 0.4087 |
| gross_profit_factor | 0.7516 |
| gross_win_rate | 0.4322 |
| sharpe_ratio | -11.5008 |
| sortino_ratio | -5.6403 |
| max_drawdown | 0.9994 |
| cagr | -0.9465 |
| net_avg_win | 10.1890 |
| net_avg_loss | -21.1980 |
| avg_hold_time_bars | 1.7923 |
| exposure | 0.0973 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
