# EMA Hourly Continuation — ALGO/USDT P12_144

**Symbol:** ALGO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.9406 |
| net_win_rate | 0.5280 |
| gross_profit_factor | 1.1049 |
| gross_win_rate | 0.5280 |
| sharpe_ratio | -0.3010 |
| sortino_ratio | -0.0778 |
| max_drawdown | 0.2477 |
| cagr | -0.0397 |
| net_avg_win | 90.0535 |
| net_avg_loss | -107.0782 |
| avg_hold_time_bars | 48.9224 |
| exposure | 0.7160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
