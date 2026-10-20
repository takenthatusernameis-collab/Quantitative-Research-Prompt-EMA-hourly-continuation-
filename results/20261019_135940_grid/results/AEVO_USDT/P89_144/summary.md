# EMA Hourly Continuation — AEVO/USDT P89_144

**Symbol:** AEVO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.5478 |
| net_win_rate | 0.4668 |
| gross_profit_factor | 0.8958 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -4.1778 |
| sortino_ratio | -1.3554 |
| max_drawdown | 0.8101 |
| cagr | -0.4736 |
| net_avg_win | 39.4830 |
| net_avg_loss | -63.0993 |
| avg_hold_time_bars | 5.0076 |
| exposure | 0.1194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
