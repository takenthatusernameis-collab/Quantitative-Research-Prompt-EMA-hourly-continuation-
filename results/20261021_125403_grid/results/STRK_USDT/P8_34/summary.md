# EMA Hourly Continuation — STRK/USDT P8_34

**Symbol:** STRK/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 724 |
| net_profit_factor | 0.7113 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.8933 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -2.6152 |
| sortino_ratio | -1.0038 |
| max_drawdown | 0.7047 |
| cagr | -0.3693 |
| net_avg_win | 48.5372 |
| net_avg_loss | -63.1592 |
| avg_hold_time_bars | 8.0552 |
| exposure | 0.2651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
