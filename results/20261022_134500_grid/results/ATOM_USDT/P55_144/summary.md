# EMA Hourly Continuation — ATOM/USDT P55_144

**Symbol:** ATOM/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.6297 |
| net_win_rate | 0.5055 |
| gross_profit_factor | 1.0131 |
| gross_win_rate | 0.5121 |
| sharpe_ratio | -2.8347 |
| sortino_ratio | -0.8502 |
| max_drawdown | 0.6548 |
| cagr | -0.3368 |
| net_avg_win | 47.5754 |
| net_avg_loss | -77.2308 |
| avg_hold_time_bars | 10.9692 |
| exposure | 0.2269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
