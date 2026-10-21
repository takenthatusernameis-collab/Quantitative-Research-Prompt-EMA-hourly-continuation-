# EMA Hourly Continuation — FLUX/USDT P89_144

**Symbol:** FLUX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.8825 |
| net_win_rate | 0.5408 |
| gross_profit_factor | 1.1597 |
| gross_win_rate | 0.5408 |
| sharpe_ratio | -0.5827 |
| sortino_ratio | -0.1446 |
| max_drawdown | 0.1808 |
| cagr | -0.0668 |
| net_avg_win | 75.3433 |
| net_avg_loss | -100.5474 |
| avg_hold_time_bars | 7.2755 |
| exposure | 0.0972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
