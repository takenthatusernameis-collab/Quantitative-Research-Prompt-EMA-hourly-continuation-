# EMA Hourly Continuation — TURBO/USDT P12_20

**Symbol:** TURBO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.8282 |
| net_win_rate | 0.5341 |
| gross_profit_factor | 1.1354 |
| gross_win_rate | 0.5341 |
| sharpe_ratio | -0.9899 |
| sortino_ratio | -0.2475 |
| max_drawdown | 0.2509 |
| cagr | -0.1076 |
| net_avg_win | 76.8356 |
| net_avg_loss | -106.3661 |
| avg_hold_time_bars | 4.1767 |
| exposure | 0.0567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
