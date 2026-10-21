# EMA Hourly Continuation — XLM/USDT P8_100

**Symbol:** XLM/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.8208 |
| net_win_rate | 0.5188 |
| gross_profit_factor | 1.0651 |
| gross_win_rate | 0.5188 |
| sharpe_ratio | -1.2539 |
| sortino_ratio | -0.3938 |
| max_drawdown | 0.3933 |
| cagr | -0.1676 |
| net_avg_win | 68.1845 |
| net_avg_loss | -89.5711 |
| avg_hold_time_bars | 30.3808 |
| exposure | 0.6601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
