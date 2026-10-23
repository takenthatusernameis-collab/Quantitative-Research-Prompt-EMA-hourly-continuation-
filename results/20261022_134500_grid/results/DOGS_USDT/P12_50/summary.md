# EMA Hourly Continuation — DOGS/USDT P12_50

**Symbol:** DOGS/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 943 |
| net_profit_factor | 0.5286 |
| net_win_rate | 0.4411 |
| gross_profit_factor | 0.8171 |
| gross_win_rate | 0.4507 |
| sharpe_ratio | -7.1846 |
| sortino_ratio | -3.3280 |
| max_drawdown | 0.9710 |
| cagr | -0.8065 |
| net_avg_win | 26.1653 |
| net_avg_loss | -39.0755 |
| avg_hold_time_bars | 6.9364 |
| exposure | 0.3470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
