# EMA Hourly Continuation — MASK/USDT P55_144

**Symbol:** MASK/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.7196 |
| net_win_rate | 0.5113 |
| gross_profit_factor | 1.0416 |
| gross_win_rate | 0.5164 |
| sharpe_ratio | -1.9106 |
| sortino_ratio | -0.5419 |
| max_drawdown | 0.4845 |
| cagr | -0.2238 |
| net_avg_win | 59.4948 |
| net_avg_loss | -86.5152 |
| avg_hold_time_bars | 12.7330 |
| exposure | 0.2298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
