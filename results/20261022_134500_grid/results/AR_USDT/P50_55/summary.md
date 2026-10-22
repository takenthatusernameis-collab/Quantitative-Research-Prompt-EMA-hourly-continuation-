# EMA Hourly Continuation — AR/USDT P50_55

**Symbol:** AR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 826 |
| net_profit_factor | 0.2074 |
| net_win_rate | 0.3680 |
| gross_profit_factor | 0.5408 |
| gross_win_rate | 0.4116 |
| sharpe_ratio | -11.3565 |
| sortino_ratio | -4.7269 |
| max_drawdown | 0.9982 |
| cagr | -0.9190 |
| net_avg_win | 8.5907 |
| net_avg_loss | -24.1253 |
| avg_hold_time_bars | 1.9976 |
| exposure | 0.0750 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
