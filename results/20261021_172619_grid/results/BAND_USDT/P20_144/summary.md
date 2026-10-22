# EMA Hourly Continuation — BAND/USDT P20_144

**Symbol:** BAND/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.7172 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.9090 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -2.2557 |
| sortino_ratio | -0.6495 |
| max_drawdown | 0.5426 |
| cagr | -0.2590 |
| net_avg_win | 68.9746 |
| net_avg_loss | -86.0314 |
| avg_hold_time_bars | 28.5061 |
| exposure | 0.5327 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
