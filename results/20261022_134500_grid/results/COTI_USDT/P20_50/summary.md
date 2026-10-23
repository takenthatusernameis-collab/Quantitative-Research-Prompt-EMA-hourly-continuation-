# EMA Hourly Continuation — COTI/USDT P20_50

**Symbol:** COTI/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1068 |
| net_profit_factor | 0.5848 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.9484 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -6.8353 |
| sortino_ratio | -3.1622 |
| max_drawdown | 0.9782 |
| cagr | -0.7802 |
| net_avg_win | 28.2793 |
| net_avg_loss | -40.5325 |
| avg_hold_time_bars | 4.3137 |
| exposure | 0.2094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
