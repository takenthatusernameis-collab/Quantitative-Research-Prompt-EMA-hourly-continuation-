# EMA Hourly Continuation — IOTA/USDT P20_89

**Symbol:** IOTA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.5337 |
| net_win_rate | 0.4386 |
| gross_profit_factor | 0.8579 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -5.3871 |
| sortino_ratio | -2.0162 |
| max_drawdown | 0.9170 |
| cagr | -0.6199 |
| net_avg_win | 33.5549 |
| net_avg_loss | -49.1319 |
| avg_hold_time_bars | 12.1693 |
| exposure | 0.3922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
