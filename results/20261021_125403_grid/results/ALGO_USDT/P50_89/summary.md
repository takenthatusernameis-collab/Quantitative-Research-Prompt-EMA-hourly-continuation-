# EMA Hourly Continuation — ALGO/USDT P50_89

**Symbol:** ALGO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.7087 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 0.9707 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -1.8532 |
| sortino_ratio | -0.4703 |
| max_drawdown | 0.4282 |
| cagr | -0.1939 |
| net_avg_win | 65.5968 |
| net_avg_loss | -90.8023 |
| avg_hold_time_bars | 6.9042 |
| exposure | 0.0982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
