# EMA Hourly Continuation — TAIKO/USDT P26_144

**Symbol:** TAIKO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.7507 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9263 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -1.6490 |
| sortino_ratio | -0.4358 |
| max_drawdown | 0.4037 |
| cagr | -0.1820 |
| net_avg_win | 72.8044 |
| net_avg_loss | -90.6372 |
| avg_hold_time_bars | 31.0985 |
| exposure | 0.4855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
