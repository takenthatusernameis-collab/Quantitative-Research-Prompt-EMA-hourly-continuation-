# EMA Hourly Continuation — CSPR/USDT P34_55

**Symbol:** CSPR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.6290 |
| net_win_rate | 0.4549 |
| gross_profit_factor | 0.8445 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -2.4925 |
| sortino_ratio | -0.6025 |
| max_drawdown | 0.5026 |
| cagr | -0.2413 |
| net_avg_win | 64.7282 |
| net_avg_loss | -85.8673 |
| avg_hold_time_bars | 5.5590 |
| exposure | 0.0728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
