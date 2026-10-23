# EMA Hourly Continuation — ZPAY/USDT P20_34

**Symbol:** ZPAY/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 937 |
| net_profit_factor | 0.3775 |
| net_win_rate | 0.3330 |
| gross_profit_factor | 0.6499 |
| gross_win_rate | 0.3404 |
| sharpe_ratio | -9.9590 |
| sortino_ratio | -4.2735 |
| max_drawdown | 0.9943 |
| cagr | -0.8715 |
| net_avg_win | 19.3300 |
| net_avg_loss | -25.5590 |
| avg_hold_time_bars | 5.8036 |
| exposure | 0.2461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
