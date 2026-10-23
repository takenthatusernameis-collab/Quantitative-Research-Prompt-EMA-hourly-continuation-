# EMA Hourly Continuation — MOVR/USDT P26_89

**Symbol:** MOVR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 758 |
| net_profit_factor | 0.5248 |
| net_win_rate | 0.4446 |
| gross_profit_factor | 0.8546 |
| gross_win_rate | 0.4565 |
| sharpe_ratio | -5.4448 |
| sortino_ratio | -2.1020 |
| max_drawdown | 0.9293 |
| cagr | -0.6379 |
| net_avg_win | 30.2191 |
| net_avg_loss | -46.0904 |
| avg_hold_time_bars | 8.6412 |
| exposure | 0.2977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
