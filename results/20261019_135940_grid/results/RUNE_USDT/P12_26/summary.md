# EMA Hourly Continuation — RUNE/USDT P12_26

**Symbol:** RUNE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1383 |
| net_profit_factor | 0.3723 |
| net_win_rate | 0.4215 |
| gross_profit_factor | 0.8043 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -11.8128 |
| sortino_ratio | -6.2014 |
| max_drawdown | 0.9997 |
| cagr | -0.9592 |
| net_avg_win | 10.1698 |
| net_avg_loss | -19.9072 |
| avg_hold_time_bars | 2.8192 |
| exposure | 0.1772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
