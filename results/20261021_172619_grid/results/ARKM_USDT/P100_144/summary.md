# EMA Hourly Continuation — ARKM/USDT P100_144

**Symbol:** ARKM/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.7056 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9143 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -1.5459 |
| sortino_ratio | -0.3390 |
| max_drawdown | 0.3387 |
| cagr | -0.1442 |
| net_avg_win | 68.0374 |
| net_avg_loss | -90.8513 |
| avg_hold_time_bars | 6.4383 |
| exposure | 0.0688 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
