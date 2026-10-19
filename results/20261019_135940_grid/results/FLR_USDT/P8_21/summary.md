# EMA Hourly Continuation — FLR/USDT P8_21

**Symbol:** FLR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1904 |
| net_profit_factor | 0.3152 |
| net_win_rate | 0.3971 |
| gross_profit_factor | 0.8215 |
| gross_win_rate | 0.4359 |
| sharpe_ratio | -15.6711 |
| sortino_ratio | -9.7569 |
| max_drawdown | 1.0000 |
| cagr | -0.9933 |
| net_avg_win | 6.0878 |
| net_avg_loss | -12.7198 |
| avg_hold_time_bars | 2.7810 |
| exposure | 0.2407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
