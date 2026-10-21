# EMA Hourly Continuation — CYBER/USDT P21_89

**Symbol:** CYBER/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 554 |
| net_profit_factor | 0.6891 |
| net_win_rate | 0.4657 |
| gross_profit_factor | 0.8710 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -2.8388 |
| sortino_ratio | -0.9504 |
| max_drawdown | 0.6793 |
| cagr | -0.3538 |
| net_avg_win | 57.2032 |
| net_avg_loss | -72.3570 |
| avg_hold_time_bars | 14.7960 |
| exposure | 0.3726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
