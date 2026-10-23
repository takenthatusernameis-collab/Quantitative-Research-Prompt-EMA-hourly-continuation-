# EMA Hourly Continuation — FLIP/USDT P12_34

**Symbol:** FLIP/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 854 |
| net_profit_factor | 0.4130 |
| net_win_rate | 0.3876 |
| gross_profit_factor | 0.8196 |
| gross_win_rate | 0.4297 |
| sharpe_ratio | -9.3723 |
| sortino_ratio | -3.8754 |
| max_drawdown | 0.9933 |
| cagr | -0.8629 |
| net_avg_win | 21.1123 |
| net_avg_loss | -32.3520 |
| avg_hold_time_bars | 8.1979 |
| exposure | 0.3182 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
