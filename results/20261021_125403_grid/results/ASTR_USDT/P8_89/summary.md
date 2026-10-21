# EMA Hourly Continuation — ASTR/USDT P8_89

**Symbol:** ASTR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.8177 |
| net_win_rate | 0.5155 |
| gross_profit_factor | 1.0563 |
| gross_win_rate | 0.5155 |
| sharpe_ratio | -1.4711 |
| sortino_ratio | -0.4918 |
| max_drawdown | 0.4650 |
| cagr | -0.2047 |
| net_avg_win | 69.7990 |
| net_avg_loss | -90.8333 |
| avg_hold_time_bars | 25.4717 |
| exposure | 0.6305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
