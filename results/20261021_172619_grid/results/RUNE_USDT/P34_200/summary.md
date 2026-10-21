# EMA Hourly Continuation — RUNE/USDT P34_200

**Symbol:** RUNE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 243 |
| net_profit_factor | 0.9579 |
| net_win_rate | 0.5391 |
| gross_profit_factor | 1.1654 |
| gross_win_rate | 0.5391 |
| sharpe_ratio | -0.1582 |
| sortino_ratio | -0.0357 |
| max_drawdown | 0.1624 |
| cagr | -0.0202 |
| net_avg_win | 86.8039 |
| net_avg_loss | -105.9879 |
| avg_hold_time_bars | 51.9588 |
| exposure | 0.5739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
