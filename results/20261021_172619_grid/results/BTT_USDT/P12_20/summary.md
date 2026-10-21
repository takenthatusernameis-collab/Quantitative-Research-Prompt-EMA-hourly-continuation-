# EMA Hourly Continuation — BTT/USDT P12_20

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.3990 |
| net_win_rate | 0.4085 |
| gross_profit_factor | 0.7569 |
| gross_win_rate | 0.4085 |
| sharpe_ratio | -5.5441 |
| sortino_ratio | -1.4169 |
| max_drawdown | 0.8173 |
| cagr | -0.4902 |
| net_avg_win | 43.3343 |
| net_avg_loss | -75.0018 |
| avg_hold_time_bars | 5.9379 |
| exposure | 0.0826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
