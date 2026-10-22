# EMA Hourly Continuation — PYTH/USDT P8_34

**Symbol:** PYTH/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1373 |
| net_profit_factor | 0.5833 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.9786 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -7.0015 |
| sortino_ratio | -3.6297 |
| max_drawdown | 0.9887 |
| cagr | -0.8301 |
| net_avg_win | 21.4474 |
| net_avg_loss | -32.5782 |
| avg_hold_time_bars | 5.1966 |
| exposure | 0.3243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
