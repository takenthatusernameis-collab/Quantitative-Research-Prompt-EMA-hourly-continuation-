# EMA Hourly Continuation — ENA/USDT P8_55

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.9578 |
| net_win_rate | 0.5303 |
| gross_profit_factor | 1.1156 |
| gross_win_rate | 0.5303 |
| sharpe_ratio | -0.2577 |
| sortino_ratio | -0.0932 |
| max_drawdown | 0.2736 |
| cagr | -0.0518 |
| net_avg_win | 85.1711 |
| net_avg_loss | -100.3832 |
| avg_hold_time_bars | 15.5685 |
| exposure | 0.4444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
