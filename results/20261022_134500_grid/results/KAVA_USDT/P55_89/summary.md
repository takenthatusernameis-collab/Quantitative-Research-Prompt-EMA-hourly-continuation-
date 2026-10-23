# EMA Hourly Continuation — KAVA/USDT P55_89

**Symbol:** KAVA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.4135 |
| net_win_rate | 0.4045 |
| gross_profit_factor | 0.8586 |
| gross_win_rate | 0.4421 |
| sharpe_ratio | -8.7531 |
| sortino_ratio | -3.3397 |
| max_drawdown | 0.9869 |
| cagr | -0.8181 |
| net_avg_win | 23.9716 |
| net_avg_loss | -39.3755 |
| avg_hold_time_bars | 4.6667 |
| exposure | 0.1521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
