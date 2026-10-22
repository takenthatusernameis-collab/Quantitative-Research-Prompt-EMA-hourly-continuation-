# EMA Hourly Continuation — TAIKO/USDT P8_21

**Symbol:** TAIKO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.8340 |
| net_win_rate | 0.5447 |
| gross_profit_factor | 1.1918 |
| gross_win_rate | 0.5447 |
| sharpe_ratio | -1.4831 |
| sortino_ratio | -0.5271 |
| max_drawdown | 0.5270 |
| cagr | -0.2161 |
| net_avg_win | 70.9711 |
| net_avg_loss | -101.7910 |
| avg_hold_time_bars | 6.2259 |
| exposure | 0.1708 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
