# EMA Hourly Continuation — DEEP/USDT P12_26

**Symbol:** DEEP/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.9786 |
| net_win_rate | 0.5627 |
| gross_profit_factor | 1.2711 |
| gross_win_rate | 0.5627 |
| sharpe_ratio | -0.0973 |
| sortino_ratio | -0.0312 |
| max_drawdown | 0.2997 |
| cagr | -0.0230 |
| net_avg_win | 95.3685 |
| net_avg_loss | -125.3774 |
| avg_hold_time_bars | 4.9233 |
| exposure | 0.1090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
