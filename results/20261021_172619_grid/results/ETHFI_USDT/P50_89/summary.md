# EMA Hourly Continuation — ETHFI/USDT P50_89

**Symbol:** ETHFI/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.8166 |
| net_win_rate | 0.5075 |
| gross_profit_factor | 1.0269 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -1.1499 |
| sortino_ratio | -0.3022 |
| max_drawdown | 0.3197 |
| cagr | -0.1308 |
| net_avg_win | 77.7063 |
| net_avg_loss | -98.0400 |
| avg_hold_time_bars | 6.9552 |
| exposure | 0.1059 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
