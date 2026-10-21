# EMA Hourly Continuation — ASTR/USDT P12_50

**Symbol:** ASTR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 673 |
| net_profit_factor | 0.7541 |
| net_win_rate | 0.4993 |
| gross_profit_factor | 1.0430 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -2.8025 |
| sortino_ratio | -1.0372 |
| max_drawdown | 0.7128 |
| cagr | -0.3819 |
| net_avg_win | 64.1688 |
| net_avg_loss | -84.8361 |
| avg_hold_time_bars | 11.9554 |
| exposure | 0.3641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
