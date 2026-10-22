# EMA Hourly Continuation — JST/USDT P20_50

**Symbol:** JST/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 853 |
| net_profit_factor | 0.2505 |
| net_win_rate | 0.4127 |
| gross_profit_factor | 0.9667 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -9.6429 |
| sortino_ratio | -4.0244 |
| max_drawdown | 0.9947 |
| cagr | -0.8729 |
| net_avg_win | 9.4424 |
| net_avg_loss | -26.4845 |
| avg_hold_time_bars | 5.4994 |
| exposure | 0.2123 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
