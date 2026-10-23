# EMA Hourly Continuation — BRETT/USDT P26_144

**Symbol:** BRETT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.6545 |
| net_win_rate | 0.4559 |
| gross_profit_factor | 0.8374 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -2.7948 |
| sortino_ratio | -0.8148 |
| max_drawdown | 0.6007 |
| cagr | -0.3202 |
| net_avg_win | 61.0757 |
| net_avg_loss | -78.1846 |
| avg_hold_time_bars | 27.0931 |
| exposure | 0.5319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
