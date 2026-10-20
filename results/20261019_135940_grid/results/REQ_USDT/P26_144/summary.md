# EMA Hourly Continuation — REQ/USDT P26_144

**Symbol:** REQ/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.5324 |
| net_win_rate | 0.4334 |
| gross_profit_factor | 0.9353 |
| gross_win_rate | 0.4527 |
| sharpe_ratio | -6.4234 |
| sortino_ratio | -2.3623 |
| max_drawdown | 0.9454 |
| cagr | -0.6838 |
| net_avg_win | 36.7039 |
| net_avg_loss | -52.7396 |
| avg_hold_time_bars | 14.7722 |
| exposure | 0.4539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
