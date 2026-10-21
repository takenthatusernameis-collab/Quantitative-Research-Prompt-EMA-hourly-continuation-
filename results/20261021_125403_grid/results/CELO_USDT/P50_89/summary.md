# EMA Hourly Continuation — CELO/USDT P50_89

**Symbol:** CELO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.9625 |
| net_win_rate | 0.5665 |
| gross_profit_factor | 1.3036 |
| gross_win_rate | 0.5665 |
| sharpe_ratio | -0.1611 |
| sortino_ratio | -0.0436 |
| max_drawdown | 0.1471 |
| cagr | -0.0253 |
| net_avg_win | 81.9922 |
| net_avg_loss | -111.3073 |
| avg_hold_time_bars | 8.2630 |
| exposure | 0.1294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
