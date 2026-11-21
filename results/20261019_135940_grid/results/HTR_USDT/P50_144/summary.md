# EMA Hourly Continuation — HTR/USDT P50_144

**Symbol:** HTR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.4497 |
| net_win_rate | 0.3890 |
| gross_profit_factor | 0.6729 |
| gross_win_rate | 0.3982 |
| sharpe_ratio | -6.9314 |
| sortino_ratio | -2.4860 |
| max_drawdown | 0.9586 |
| cagr | -0.7070 |
| net_avg_win | 30.7026 |
| net_avg_loss | -43.4592 |
| avg_hold_time_bars | 8.4625 |
| exposure | 0.2512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
