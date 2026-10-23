# EMA Hourly Continuation — CELR/USDT P8_26

**Symbol:** CELR/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1488 |
| net_profit_factor | 0.4233 |
| net_win_rate | 0.4402 |
| gross_profit_factor | 0.8693 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -9.5347 |
| sortino_ratio | -5.1763 |
| max_drawdown | 0.9983 |
| cagr | -0.9199 |
| net_avg_win | 11.1872 |
| net_avg_loss | -20.7809 |
| avg_hold_time_bars | 4.4254 |
| exposure | 0.2980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
