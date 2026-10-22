# EMA Hourly Continuation — EIGEN/USDT P50_144

**Symbol:** EIGEN/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.7277 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 1.0154 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -2.5447 |
| sortino_ratio | -0.8406 |
| max_drawdown | 0.6007 |
| cagr | -0.3304 |
| net_avg_win | 67.5130 |
| net_avg_loss | -91.5380 |
| avg_hold_time_bars | 10.7472 |
| exposure | 0.2673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
