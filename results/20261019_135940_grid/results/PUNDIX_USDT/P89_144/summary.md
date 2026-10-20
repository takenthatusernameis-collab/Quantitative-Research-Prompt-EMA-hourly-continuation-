# EMA Hourly Continuation — PUNDIX/USDT P89_144

**Symbol:** PUNDIX/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.4531 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8926 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -5.2443 |
| sortino_ratio | -1.6532 |
| max_drawdown | 0.8693 |
| cagr | -0.5540 |
| net_avg_win | 31.6980 |
| net_avg_loss | -59.2516 |
| avg_hold_time_bars | 6.7717 |
| exposure | 0.1524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
