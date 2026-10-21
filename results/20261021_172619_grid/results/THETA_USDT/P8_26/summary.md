# EMA Hourly Continuation — THETA/USDT P8_26

**Symbol:** THETA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.8233 |
| net_win_rate | 0.5227 |
| gross_profit_factor | 1.0964 |
| gross_win_rate | 0.5227 |
| sharpe_ratio | -1.6333 |
| sortino_ratio | -0.6156 |
| max_drawdown | 0.5206 |
| cagr | -0.2475 |
| net_avg_win | 66.5840 |
| net_avg_loss | -88.5703 |
| avg_hold_time_bars | 6.6603 |
| exposure | 0.2068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
