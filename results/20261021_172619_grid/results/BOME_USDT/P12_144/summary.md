# EMA Hourly Continuation — BOME/USDT P12_144

**Symbol:** BOME/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.8210 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9471 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -1.2233 |
| sortino_ratio | -0.3456 |
| max_drawdown | 0.3860 |
| cagr | -0.1491 |
| net_avg_win | 79.6624 |
| net_avg_loss | -92.6811 |
| avg_hold_time_bars | 37.1094 |
| exposure | 0.6629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
