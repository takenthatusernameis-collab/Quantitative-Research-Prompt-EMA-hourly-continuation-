# EMA Hourly Continuation — SUSHI/USDT P20_89

**Symbol:** SUSHI/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7498 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9416 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -2.0839 |
| sortino_ratio | -0.6693 |
| max_drawdown | 0.5689 |
| cagr | -0.2652 |
| net_avg_win | 65.8367 |
| net_avg_loss | -82.4425 |
| avg_hold_time_bars | 16.3346 |
| exposure | 0.3755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
