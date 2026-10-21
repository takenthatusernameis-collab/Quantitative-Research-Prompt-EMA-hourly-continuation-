# EMA Hourly Continuation — DEGEN/USDT P21_34

**Symbol:** DEGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.7923 |
| net_win_rate | 0.5058 |
| gross_profit_factor | 1.0137 |
| gross_win_rate | 0.5058 |
| sharpe_ratio | -1.3882 |
| sortino_ratio | -0.3697 |
| max_drawdown | 0.4550 |
| cagr | -0.1569 |
| net_avg_win | 76.3361 |
| net_avg_loss | -98.6089 |
| avg_hold_time_bars | 5.8488 |
| exposure | 0.0916 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
