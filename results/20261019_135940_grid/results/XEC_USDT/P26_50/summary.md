# EMA Hourly Continuation — XEC/USDT P26_50

**Symbol:** XEC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1033 |
| net_profit_factor | 0.4628 |
| net_win_rate | 0.4482 |
| gross_profit_factor | 1.0217 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -8.5090 |
| sortino_ratio | -3.8753 |
| max_drawdown | 0.9921 |
| cagr | -0.8532 |
| net_avg_win | 18.4592 |
| net_avg_loss | -32.3992 |
| avg_hold_time_bars | 4.2517 |
| exposure | 0.1987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
