# EMA Hourly Continuation — VELO/USDT P26_144

**Symbol:** VELO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.9036 |
| net_win_rate | 0.5164 |
| gross_profit_factor | 1.0498 |
| gross_win_rate | 0.5164 |
| sharpe_ratio | -0.5658 |
| sortino_ratio | -0.1619 |
| max_drawdown | 0.3095 |
| cagr | -0.0760 |
| net_avg_win | 82.3235 |
| net_avg_loss | -97.2787 |
| avg_hold_time_bars | 25.8136 |
| exposure | 0.4658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
