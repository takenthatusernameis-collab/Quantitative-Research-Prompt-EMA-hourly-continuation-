# EMA Hourly Continuation — OGN/USDT P12_20

**Symbol:** OGN/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1373 |
| net_profit_factor | 0.3356 |
| net_win_rate | 0.4050 |
| gross_profit_factor | 0.9293 |
| gross_win_rate | 0.4603 |
| sharpe_ratio | -12.8942 |
| sortino_ratio | -6.8050 |
| max_drawdown | 0.9999 |
| cagr | -0.9704 |
| net_avg_win | 9.0856 |
| net_avg_loss | -18.4213 |
| avg_hold_time_bars | 2.7007 |
| exposure | 0.1678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
