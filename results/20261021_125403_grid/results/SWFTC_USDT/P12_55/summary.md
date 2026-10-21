# EMA Hourly Continuation — SWFTC/USDT P12_55

**Symbol:** SWFTC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.7342 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9350 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -2.3595 |
| sortino_ratio | -0.8141 |
| max_drawdown | 0.6182 |
| cagr | -0.3116 |
| net_avg_win | 59.6151 |
| net_avg_loss | -75.8162 |
| avg_hold_time_bars | 11.4503 |
| exposure | 0.3040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
