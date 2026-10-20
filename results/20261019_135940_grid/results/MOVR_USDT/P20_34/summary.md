# EMA Hourly Continuation — MOVR/USDT P20_34

**Symbol:** MOVR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1196 |
| net_profit_factor | 0.3264 |
| net_win_rate | 0.4156 |
| gross_profit_factor | 0.7600 |
| gross_win_rate | 0.4465 |
| sharpe_ratio | -10.2111 |
| sortino_ratio | -4.9898 |
| max_drawdown | 0.9982 |
| cagr | -0.9192 |
| net_avg_win | 9.7304 |
| net_avg_loss | -21.1988 |
| avg_hold_time_bars | 2.8855 |
| exposure | 0.1569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
