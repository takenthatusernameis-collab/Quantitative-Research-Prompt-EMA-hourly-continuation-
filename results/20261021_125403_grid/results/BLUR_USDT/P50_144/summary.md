# EMA Hourly Continuation — BLUR/USDT P50_144

**Symbol:** BLUR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.8811 |
| net_win_rate | 0.5306 |
| gross_profit_factor | 1.1169 |
| gross_win_rate | 0.5306 |
| sharpe_ratio | -0.7029 |
| sortino_ratio | -0.1917 |
| max_drawdown | 0.2629 |
| cagr | -0.0874 |
| net_avg_win | 80.0072 |
| net_avg_loss | -102.6193 |
| avg_hold_time_bars | 17.7944 |
| exposure | 0.2899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
