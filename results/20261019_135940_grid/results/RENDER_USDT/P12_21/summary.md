# EMA Hourly Continuation — RENDER/USDT P12_21

**Symbol:** RENDER/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1268 |
| net_profit_factor | 0.4257 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.8723 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -12.0042 |
| sortino_ratio | -6.4873 |
| max_drawdown | 0.9994 |
| cagr | -0.9660 |
| net_avg_win | 13.5652 |
| net_avg_loss | -24.0996 |
| avg_hold_time_bars | 2.2603 |
| exposure | 0.1513 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
