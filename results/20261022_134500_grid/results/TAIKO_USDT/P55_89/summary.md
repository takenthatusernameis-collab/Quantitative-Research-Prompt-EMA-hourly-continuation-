# EMA Hourly Continuation — TAIKO/USDT P55_89

**Symbol:** TAIKO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.4532 |
| net_win_rate | 0.4315 |
| gross_profit_factor | 0.7920 |
| gross_win_rate | 0.4518 |
| sharpe_ratio | -6.4826 |
| sortino_ratio | -2.2957 |
| max_drawdown | 0.9331 |
| cagr | -0.6763 |
| net_avg_win | 30.2770 |
| net_avg_loss | -50.7005 |
| avg_hold_time_bars | 4.3486 |
| exposure | 0.1235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
