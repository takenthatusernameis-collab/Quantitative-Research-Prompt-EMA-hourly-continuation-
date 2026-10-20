# EMA Hourly Continuation — TURBO/USDT P12_50

**Symbol:** TURBO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 940 |
| net_profit_factor | 0.6875 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 1.0183 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -4.9564 |
| sortino_ratio | -2.3507 |
| max_drawdown | 0.9092 |
| cagr | -0.6718 |
| net_avg_win | 43.5527 |
| net_avg_loss | -59.6870 |
| avg_hold_time_bars | 6.2021 |
| exposure | 0.3181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
