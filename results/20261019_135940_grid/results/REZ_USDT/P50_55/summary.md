# EMA Hourly Continuation — REZ/USDT P50_55

**Symbol:** REZ/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 822 |
| net_profit_factor | 0.3283 |
| net_win_rate | 0.4015 |
| gross_profit_factor | 0.7478 |
| gross_win_rate | 0.4465 |
| sharpe_ratio | -9.6138 |
| sortino_ratio | -3.9756 |
| max_drawdown | 0.9939 |
| cagr | -0.8729 |
| net_avg_win | 14.7196 |
| net_avg_loss | -30.0746 |
| avg_hold_time_bars | 2.3613 |
| exposure | 0.0896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
