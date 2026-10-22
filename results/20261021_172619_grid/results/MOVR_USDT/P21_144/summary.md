# EMA Hourly Continuation — MOVR/USDT P21_144

**Symbol:** MOVR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6634 |
| net_win_rate | 0.4464 |
| gross_profit_factor | 0.7970 |
| gross_win_rate | 0.4464 |
| sharpe_ratio | -2.6707 |
| sortino_ratio | -0.8159 |
| max_drawdown | 0.6338 |
| cagr | -0.3137 |
| net_avg_win | 57.9295 |
| net_avg_loss | -70.4018 |
| avg_hold_time_bars | 23.5215 |
| exposure | 0.4982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
