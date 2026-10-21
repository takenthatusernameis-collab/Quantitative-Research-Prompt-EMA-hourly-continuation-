# EMA Hourly Continuation — DCR/USDT P50_100

**Symbol:** DCR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.5838 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.8134 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -3.2779 |
| sortino_ratio | -0.9476 |
| max_drawdown | 0.6753 |
| cagr | -0.3537 |
| net_avg_win | 50.0652 |
| net_avg_loss | -70.6484 |
| avg_hold_time_bars | 9.3647 |
| exposure | 0.1754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
