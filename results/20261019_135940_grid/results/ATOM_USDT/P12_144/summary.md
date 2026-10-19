# EMA Hourly Continuation — ATOM/USDT P12_144

**Symbol:** ATOM/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.6717 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0337 |
| gross_win_rate | 0.5062 |
| sharpe_ratio | -2.7120 |
| sortino_ratio | -0.8363 |
| max_drawdown | 0.6518 |
| cagr | -0.3316 |
| net_avg_win | 54.0359 |
| net_avg_loss | -80.4415 |
| avg_hold_time_bars | 30.1909 |
| exposure | 0.6615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
