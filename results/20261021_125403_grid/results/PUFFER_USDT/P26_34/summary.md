# EMA Hourly Continuation — PUFFER/USDT P26_34

**Symbol:** PUFFER/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 191 |
| net_profit_factor | 0.7260 |
| net_win_rate | 0.5026 |
| gross_profit_factor | 1.0039 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -1.5056 |
| sortino_ratio | -0.3331 |
| max_drawdown | 0.2657 |
| cagr | -0.1420 |
| net_avg_win | 73.3402 |
| net_avg_loss | -102.0851 |
| avg_hold_time_bars | 6.3874 |
| exposure | 0.0690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
