# EMA Hourly Continuation — CGPT/USDT P12_200

**Symbol:** CGPT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.8499 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9628 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -0.7630 |
| sortino_ratio | -0.1744 |
| max_drawdown | 0.2077 |
| cagr | -0.0792 |
| net_avg_win | 84.0853 |
| net_avg_loss | -95.8877 |
| avg_hold_time_bars | 65.6758 |
| exposure | 0.7642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
