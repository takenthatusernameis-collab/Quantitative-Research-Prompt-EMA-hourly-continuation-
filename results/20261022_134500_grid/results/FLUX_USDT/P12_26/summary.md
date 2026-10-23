# EMA Hourly Continuation — FLUX/USDT P12_26

**Symbol:** FLUX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1397 |
| net_profit_factor | 0.4293 |
| net_win_rate | 0.4395 |
| gross_profit_factor | 0.8704 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -10.3347 |
| sortino_ratio | -5.4597 |
| max_drawdown | 0.9989 |
| cagr | -0.9345 |
| net_avg_win | 12.2394 |
| net_avg_loss | -22.3555 |
| avg_hold_time_bars | 2.7731 |
| exposure | 0.1761 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
