# EMA Hourly Continuation — MOVR/USDT P12_21

**Symbol:** MOVR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1549 |
| net_profit_factor | 0.3079 |
| net_win_rate | 0.4138 |
| gross_profit_factor | 0.7822 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -12.4336 |
| sortino_ratio | -6.9478 |
| max_drawdown | 0.9999 |
| cagr | -0.9700 |
| net_avg_win | 6.9404 |
| net_avg_loss | -15.9112 |
| avg_hold_time_bars | 2.4700 |
| exposure | 0.1739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
