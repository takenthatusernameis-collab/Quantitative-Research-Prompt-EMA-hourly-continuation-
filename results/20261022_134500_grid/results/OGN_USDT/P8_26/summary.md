# EMA Hourly Continuation — OGN/USDT P8_26

**Symbol:** OGN/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1456 |
| net_profit_factor | 0.4470 |
| net_win_rate | 0.4361 |
| gross_profit_factor | 0.9429 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -10.2029 |
| sortino_ratio | -5.4639 |
| max_drawdown | 0.9990 |
| cagr | -0.9348 |
| net_avg_win | 12.7158 |
| net_avg_loss | -22.0029 |
| avg_hold_time_bars | 4.4622 |
| exposure | 0.2940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
