# EMA Hourly Continuation — TFUEL/USDT P20_50

**Symbol:** TFUEL/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.5392 |
| net_win_rate | 0.4156 |
| gross_profit_factor | 0.7661 |
| gross_win_rate | 0.4156 |
| sharpe_ratio | -5.1395 |
| sortino_ratio | -1.7137 |
| max_drawdown | 0.8667 |
| cagr | -0.5469 |
| net_avg_win | 44.1708 |
| net_avg_loss | -58.2544 |
| avg_hold_time_bars | 7.7187 |
| exposure | 0.1925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
