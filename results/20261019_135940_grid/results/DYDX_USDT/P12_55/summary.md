# EMA Hourly Continuation — DYDX/USDT P12_55

**Symbol:** DYDX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 929 |
| net_profit_factor | 0.6333 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 1.0172 |
| gross_win_rate | 0.4876 |
| sharpe_ratio | -5.0437 |
| sortino_ratio | -2.1537 |
| max_drawdown | 0.9323 |
| cagr | -0.6470 |
| net_avg_win | 36.2908 |
| net_avg_loss | -51.7876 |
| avg_hold_time_bars | 9.7718 |
| exposure | 0.4126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
