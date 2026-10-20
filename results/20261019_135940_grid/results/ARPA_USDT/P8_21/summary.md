# EMA Hourly Continuation — ARPA/USDT P8_21

**Symbol:** ARPA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1686 |
| net_profit_factor | 0.3982 |
| net_win_rate | 0.4087 |
| gross_profit_factor | 0.9190 |
| gross_win_rate | 0.4330 |
| sharpe_ratio | -13.0084 |
| sortino_ratio | -7.5512 |
| max_drawdown | 0.9999 |
| cagr | -0.9780 |
| net_avg_win | 9.6020 |
| net_avg_loss | -16.6651 |
| avg_hold_time_bars | 3.3446 |
| exposure | 0.2552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
