# EMA Hourly Continuation — TRADE/USDT P12_21

**Symbol:** TRADE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1215 |
| net_profit_factor | 0.3530 |
| net_win_rate | 0.3605 |
| gross_profit_factor | 0.7742 |
| gross_win_rate | 0.3720 |
| sharpe_ratio | -13.3676 |
| sortino_ratio | -6.6272 |
| max_drawdown | 0.9999 |
| cagr | -0.9704 |
| net_avg_win | 12.4526 |
| net_avg_loss | -19.8878 |
| avg_hold_time_bars | 3.2988 |
| exposure | 0.1822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
