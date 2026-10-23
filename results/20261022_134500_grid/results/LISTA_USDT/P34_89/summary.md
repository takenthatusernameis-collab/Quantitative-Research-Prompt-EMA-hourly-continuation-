# EMA Hourly Continuation — LISTA/USDT P34_89

**Symbol:** LISTA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.6248 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9385 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -3.7017 |
| sortino_ratio | -1.3374 |
| max_drawdown | 0.7750 |
| cagr | -0.4699 |
| net_avg_win | 43.7792 |
| net_avg_loss | -64.5736 |
| avg_hold_time_bars | 9.0049 |
| exposure | 0.2699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
