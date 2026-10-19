# EMA Hourly Continuation — ATOM/USDT P20_55

**Symbol:** ATOM/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 889 |
| net_profit_factor | 0.4444 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.8596 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -6.9529 |
| sortino_ratio | -2.9413 |
| max_drawdown | 0.9722 |
| cagr | -0.7569 |
| net_avg_win | 19.4197 |
| net_avg_loss | -35.7487 |
| avg_hold_time_bars | 5.7424 |
| exposure | 0.2320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
