# EMA Hourly Continuation — RENDER/USDT P26_55

**Symbol:** RENDER/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.7772 |
| net_win_rate | 0.5088 |
| gross_profit_factor | 1.0171 |
| gross_win_rate | 0.5088 |
| sharpe_ratio | -1.4817 |
| sortino_ratio | -0.4229 |
| max_drawdown | 0.4038 |
| cagr | -0.1767 |
| net_avg_win | 69.2113 |
| net_avg_loss | -92.2528 |
| avg_hold_time_bars | 6.8735 |
| exposure | 0.1233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
