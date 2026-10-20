# EMA Hourly Continuation — ORBS/USDT P34_144

**Symbol:** ORBS/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.5599 |
| net_win_rate | 0.4204 |
| gross_profit_factor | 0.9340 |
| gross_win_rate | 0.4355 |
| sharpe_ratio | -5.8732 |
| sortino_ratio | -2.0140 |
| max_drawdown | 0.9192 |
| cagr | -0.6281 |
| net_avg_win | 46.4550 |
| net_avg_loss | -60.1910 |
| avg_hold_time_bars | 14.7069 |
| exposure | 0.3991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
