# EMA Hourly Continuation — RENDER/USDT P89_100

**Symbol:** RENDER/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 90 |
| net_profit_factor | 0.7036 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9649 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -1.1591 |
| sortino_ratio | -0.1698 |
| max_drawdown | 0.2284 |
| cagr | -0.0749 |
| net_avg_win | 83.6307 |
| net_avg_loss | -113.6968 |
| avg_hold_time_bars | 5.7333 |
| exposure | 0.0272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
