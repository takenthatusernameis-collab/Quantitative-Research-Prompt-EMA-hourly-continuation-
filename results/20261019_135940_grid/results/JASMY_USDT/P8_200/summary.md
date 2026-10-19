# EMA Hourly Continuation — JASMY/USDT P8_200

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.8595 |
| net_win_rate | 0.5391 |
| gross_profit_factor | 1.1838 |
| gross_win_rate | 0.5447 |
| sharpe_ratio | -0.8464 |
| sortino_ratio | -0.2277 |
| max_drawdown | 0.3112 |
| cagr | -0.1049 |
| net_avg_win | 77.0026 |
| net_avg_loss | -104.7951 |
| avg_hold_time_bars | 49.4134 |
| exposure | 0.8041 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
