# EMA Hourly Continuation — IOST/USDT P34_200

**Symbol:** IOST/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.7223 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 1.0733 |
| gross_win_rate | 0.5202 |
| sharpe_ratio | -1.9740 |
| sortino_ratio | -0.5555 |
| max_drawdown | 0.5408 |
| cagr | -0.2338 |
| net_avg_win | 62.4703 |
| net_avg_loss | -90.9715 |
| avg_hold_time_bars | 28.0202 |
| exposure | 0.5044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
