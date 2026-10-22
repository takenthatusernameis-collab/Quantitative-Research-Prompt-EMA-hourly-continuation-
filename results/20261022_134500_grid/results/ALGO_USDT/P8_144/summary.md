# EMA Hourly Continuation — ALGO/USDT P8_144

**Symbol:** ALGO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.7901 |
| net_win_rate | 0.5193 |
| gross_profit_factor | 1.0802 |
| gross_win_rate | 0.5252 |
| sharpe_ratio | -1.2047 |
| sortino_ratio | -0.3124 |
| max_drawdown | 0.3411 |
| cagr | -0.1395 |
| net_avg_win | 67.6000 |
| net_avg_loss | -92.4236 |
| avg_hold_time_bars | 52.5638 |
| exposure | 0.8052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
