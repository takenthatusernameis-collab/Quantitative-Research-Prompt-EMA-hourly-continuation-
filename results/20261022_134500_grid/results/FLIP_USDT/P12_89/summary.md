# EMA Hourly Continuation — FLIP/USDT P12_89

**Symbol:** FLIP/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.5532 |
| net_win_rate | 0.4432 |
| gross_profit_factor | 0.8667 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -4.6918 |
| sortino_ratio | -1.4772 |
| max_drawdown | 0.8561 |
| cagr | -0.5247 |
| net_avg_win | 45.5157 |
| net_avg_loss | -65.4816 |
| avg_hold_time_bars | 25.2852 |
| exposure | 0.5965 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
