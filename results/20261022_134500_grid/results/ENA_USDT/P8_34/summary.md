# EMA Hourly Continuation — ENA/USDT P8_34

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1355 |
| net_profit_factor | 0.6481 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9591 |
| gross_win_rate | 0.4937 |
| sharpe_ratio | -5.2128 |
| sortino_ratio | -2.7091 |
| max_drawdown | 0.9635 |
| cagr | -0.7241 |
| net_avg_win | 26.6485 |
| net_avg_loss | -39.5088 |
| avg_hold_time_bars | 5.3100 |
| exposure | 0.3270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
