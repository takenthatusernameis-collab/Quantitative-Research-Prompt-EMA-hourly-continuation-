# EMA Hourly Continuation — ZPAY/USDT P50_89

**Symbol:** ZPAY/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.3836 |
| net_win_rate | 0.3415 |
| gross_profit_factor | 0.5721 |
| gross_win_rate | 0.3446 |
| sharpe_ratio | -7.4297 |
| sortino_ratio | -2.6563 |
| max_drawdown | 0.9603 |
| cagr | -0.7165 |
| net_avg_win | 26.7425 |
| net_avg_loss | -36.1570 |
| avg_hold_time_bars | 9.3553 |
| exposure | 0.2764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
