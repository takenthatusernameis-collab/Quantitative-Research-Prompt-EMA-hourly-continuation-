# EMA Hourly Continuation — MANA/USDT P55_89

**Symbol:** MANA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.6010 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8381 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -2.6955 |
| sortino_ratio | -0.6769 |
| max_drawdown | 0.5472 |
| cagr | -0.2663 |
| net_avg_win | 57.3419 |
| net_avg_loss | -81.1213 |
| avg_hold_time_bars | 6.8479 |
| exposure | 0.0962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
