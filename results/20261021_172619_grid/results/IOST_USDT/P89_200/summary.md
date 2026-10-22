# EMA Hourly Continuation — IOST/USDT P89_200

**Symbol:** IOST/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.8827 |
| net_win_rate | 0.5495 |
| gross_profit_factor | 1.2073 |
| gross_win_rate | 0.5495 |
| sharpe_ratio | -0.6194 |
| sortino_ratio | -0.1536 |
| max_drawdown | 0.2408 |
| cagr | -0.0704 |
| net_avg_win | 78.3367 |
| net_avg_loss | -108.2425 |
| avg_hold_time_bars | 14.1024 |
| exposure | 0.1878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
