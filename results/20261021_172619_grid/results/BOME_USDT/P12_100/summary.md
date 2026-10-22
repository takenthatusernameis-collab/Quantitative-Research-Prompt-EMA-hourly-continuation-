# EMA Hourly Continuation — BOME/USDT P12_100

**Symbol:** BOME/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.8075 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 0.9492 |
| gross_win_rate | 0.4918 |
| sharpe_ratio | -1.3851 |
| sortino_ratio | -0.4367 |
| max_drawdown | 0.4504 |
| cagr | -0.1840 |
| net_avg_win | 69.9169 |
| net_avg_loss | -83.7875 |
| avg_hold_time_bars | 24.4406 |
| exposure | 0.5421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
