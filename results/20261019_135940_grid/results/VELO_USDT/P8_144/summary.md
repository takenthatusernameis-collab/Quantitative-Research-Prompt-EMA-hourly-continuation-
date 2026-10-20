# EMA Hourly Continuation — VELO/USDT P8_144

**Symbol:** VELO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.7647 |
| net_win_rate | 0.5092 |
| gross_profit_factor | 1.0229 |
| gross_win_rate | 0.5108 |
| sharpe_ratio | -1.9800 |
| sortino_ratio | -0.6866 |
| max_drawdown | 0.6315 |
| cagr | -0.2795 |
| net_avg_win | 59.5675 |
| net_avg_loss | -80.8041 |
| avg_hold_time_bars | 25.7920 |
| exposure | 0.7046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
