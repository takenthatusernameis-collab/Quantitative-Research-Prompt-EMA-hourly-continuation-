# EMA Hourly Continuation — REQ/USDT P50_89

**Symbol:** REQ/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 780 |
| net_profit_factor | 0.4027 |
| net_win_rate | 0.3885 |
| gross_profit_factor | 0.9542 |
| gross_win_rate | 0.4295 |
| sharpe_ratio | -9.7920 |
| sortino_ratio | -3.9163 |
| max_drawdown | 0.9936 |
| cagr | -0.8647 |
| net_avg_win | 22.0999 |
| net_avg_loss | -34.8648 |
| avg_hold_time_bars | 4.6923 |
| exposure | 0.1664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
