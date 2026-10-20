# EMA Hourly Continuation — COTI/USDT P20_89

**Symbol:** COTI/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 776 |
| net_profit_factor | 0.6733 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 1.0050 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -3.7651 |
| sortino_ratio | -1.4708 |
| max_drawdown | 0.8387 |
| cagr | -0.5092 |
| net_avg_win | 45.4024 |
| net_avg_loss | -64.0404 |
| avg_hold_time_bars | 10.7977 |
| exposure | 0.3809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
