# EMA Hourly Continuation — SUPER/USDT P8_34

**Symbol:** SUPER/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 762 |
| net_profit_factor | 0.8072 |
| net_win_rate | 0.5171 |
| gross_profit_factor | 1.0556 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -1.7483 |
| sortino_ratio | -0.6933 |
| max_drawdown | 0.5730 |
| cagr | -0.2749 |
| net_avg_win | 58.8779 |
| net_avg_loss | -78.0901 |
| avg_hold_time_bars | 8.5892 |
| exposure | 0.2975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
