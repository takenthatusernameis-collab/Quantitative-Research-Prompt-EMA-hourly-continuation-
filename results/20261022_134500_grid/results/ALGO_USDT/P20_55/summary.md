# EMA Hourly Continuation — ALGO/USDT P20_55

**Symbol:** ALGO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 934 |
| net_profit_factor | 0.5570 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9868 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -5.5843 |
| sortino_ratio | -2.4119 |
| max_drawdown | 0.9482 |
| cagr | -0.6855 |
| net_avg_win | 26.3564 |
| net_avg_loss | -44.1802 |
| avg_hold_time_bars | 5.1724 |
| exposure | 0.2196 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
