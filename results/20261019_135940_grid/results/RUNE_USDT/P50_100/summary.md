# EMA Hourly Continuation — RUNE/USDT P50_100

**Symbol:** RUNE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.5810 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 0.9562 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -3.5734 |
| sortino_ratio | -1.2413 |
| max_drawdown | 0.7879 |
| cagr | -0.4403 |
| net_avg_win | 35.7026 |
| net_avg_loss | -62.0708 |
| avg_hold_time_bars | 7.1619 |
| exposure | 0.1930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
