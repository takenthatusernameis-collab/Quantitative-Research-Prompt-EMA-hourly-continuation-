# EMA Hourly Continuation — SHR/USDT P20_89

**Symbol:** SHR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1051 |
| net_profit_factor | 0.3994 |
| net_win_rate | 0.3359 |
| gross_profit_factor | 0.5516 |
| gross_win_rate | 0.3359 |
| sharpe_ratio | -9.6655 |
| sortino_ratio | -4.3658 |
| max_drawdown | 0.9951 |
| cagr | -0.8780 |
| net_avg_win | 18.7417 |
| net_avg_loss | -23.7339 |
| avg_hold_time_bars | 6.9363 |
| exposure | 0.3299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
