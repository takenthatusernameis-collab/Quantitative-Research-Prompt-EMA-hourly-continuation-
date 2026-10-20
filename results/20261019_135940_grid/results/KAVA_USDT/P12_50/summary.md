# EMA Hourly Continuation — KAVA/USDT P12_50

**Symbol:** KAVA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1097 |
| net_profit_factor | 0.5528 |
| net_win_rate | 0.4348 |
| gross_profit_factor | 0.9738 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -8.4820 |
| sortino_ratio | -3.9446 |
| max_drawdown | 0.9933 |
| cagr | -0.8612 |
| net_avg_win | 25.7366 |
| net_avg_loss | -35.8164 |
| avg_hold_time_bars | 7.9371 |
| exposure | 0.3958 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
