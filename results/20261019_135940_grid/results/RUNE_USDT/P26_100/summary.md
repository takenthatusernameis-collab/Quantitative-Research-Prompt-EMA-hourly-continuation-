# EMA Hourly Continuation — RUNE/USDT P26_100

**Symbol:** RUNE/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.6659 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 1.0281 |
| gross_win_rate | 0.5104 |
| sharpe_ratio | -2.9747 |
| sortino_ratio | -0.9570 |
| max_drawdown | 0.7147 |
| cagr | -0.3716 |
| net_avg_win | 51.3978 |
| net_avg_loss | -79.2666 |
| avg_hold_time_bars | 18.7647 |
| exposure | 0.4495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
