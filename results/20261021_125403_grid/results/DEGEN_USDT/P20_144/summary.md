# EMA Hourly Continuation — DEGEN/USDT P20_144

**Symbol:** DEGEN/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.9867 |
| net_win_rate | 0.5339 |
| gross_profit_factor | 1.1358 |
| gross_win_rate | 0.5339 |
| sharpe_ratio | -0.0371 |
| sortino_ratio | -0.0105 |
| max_drawdown | 0.3036 |
| cagr | -0.0123 |
| net_avg_win | 110.5162 |
| net_avg_loss | -128.2714 |
| avg_hold_time_bars | 30.8099 |
| exposure | 0.5387 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
