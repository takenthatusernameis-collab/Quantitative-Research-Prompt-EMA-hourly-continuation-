# EMA Hourly Continuation — MNT/USDT P55_144

**Symbol:** MNT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.4701 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8622 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -4.2506 |
| sortino_ratio | -1.2186 |
| max_drawdown | 0.7892 |
| cagr | -0.4504 |
| net_avg_win | 36.8916 |
| net_avg_loss | -64.9325 |
| avg_hold_time_bars | 14.1985 |
| exposure | 0.2665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
