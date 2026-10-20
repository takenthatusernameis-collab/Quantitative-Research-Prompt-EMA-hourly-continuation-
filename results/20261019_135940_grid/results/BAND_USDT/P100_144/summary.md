# EMA Hourly Continuation — BAND/USDT P100_144

**Symbol:** BAND/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.5028 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.9714 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -4.5033 |
| sortino_ratio | -1.3448 |
| max_drawdown | 0.8192 |
| cagr | -0.4870 |
| net_avg_win | 37.7796 |
| net_avg_loss | -69.1126 |
| avg_hold_time_bars | 4.6725 |
| exposure | 0.0962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
