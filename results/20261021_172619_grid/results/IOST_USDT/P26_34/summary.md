# EMA Hourly Continuation — IOST/USDT P26_34

**Symbol:** IOST/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.5880 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9552 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -3.0699 |
| sortino_ratio | -0.7749 |
| max_drawdown | 0.5954 |
| cagr | -0.3003 |
| net_avg_win | 57.1042 |
| net_avg_loss | -90.3925 |
| avg_hold_time_bars | 4.8469 |
| exposure | 0.0676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
