# EMA Hourly Continuation — OGN/USDT P50_89

**Symbol:** OGN/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.4427 |
| net_win_rate | 0.4322 |
| gross_profit_factor | 0.8388 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -6.9998 |
| sortino_ratio | -2.6281 |
| max_drawdown | 0.9639 |
| cagr | -0.7303 |
| net_avg_win | 24.7643 |
| net_avg_loss | -42.5752 |
| avg_hold_time_bars | 5.4154 |
| exposure | 0.1752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
