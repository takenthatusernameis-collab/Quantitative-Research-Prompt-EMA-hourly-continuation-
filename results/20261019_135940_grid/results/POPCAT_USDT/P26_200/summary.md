# EMA Hourly Continuation — POPCAT/USDT P26_200

**Symbol:** POPCAT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.8519 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0665 |
| gross_win_rate | 0.5139 |
| sharpe_ratio | -1.0623 |
| sortino_ratio | -0.2921 |
| max_drawdown | 0.3653 |
| cagr | -0.1305 |
| net_avg_win | 90.3659 |
| net_avg_loss | -112.1534 |
| avg_hold_time_bars | 34.2322 |
| exposure | 0.5841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
