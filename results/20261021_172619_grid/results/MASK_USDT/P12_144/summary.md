# EMA Hourly Continuation — MASK/USDT P12_144

**Symbol:** MASK/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.6483 |
| net_win_rate | 0.4644 |
| gross_profit_factor | 0.8327 |
| gross_win_rate | 0.4644 |
| sharpe_ratio | -2.6421 |
| sortino_ratio | -0.7834 |
| max_drawdown | 0.6081 |
| cagr | -0.3037 |
| net_avg_win | 54.4987 |
| net_avg_loss | -72.8761 |
| avg_hold_time_bars | 32.6713 |
| exposure | 0.6460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
