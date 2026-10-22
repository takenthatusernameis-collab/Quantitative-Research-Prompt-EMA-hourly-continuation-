# EMA Hourly Continuation — KMNO/USDT P144_200

**Symbol:** KMNO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.6294 |
| net_win_rate | 0.5074 |
| gross_profit_factor | 1.0791 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -2.9553 |
| sortino_ratio | -0.7698 |
| max_drawdown | 0.6331 |
| cagr | -0.3149 |
| net_avg_win | 59.9660 |
| net_avg_loss | -98.1301 |
| avg_hold_time_bars | 5.0649 |
| exposure | 0.0793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
