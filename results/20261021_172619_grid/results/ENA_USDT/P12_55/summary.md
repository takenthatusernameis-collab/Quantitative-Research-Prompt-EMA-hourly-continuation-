# EMA Hourly Continuation — ENA/USDT P12_55

**Symbol:** ENA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.9831 |
| net_win_rate | 0.5394 |
| gross_profit_factor | 1.1582 |
| gross_win_rate | 0.5394 |
| sharpe_ratio | -0.0528 |
| sortino_ratio | -0.0185 |
| max_drawdown | 0.2193 |
| cagr | -0.0194 |
| net_avg_win | 88.8352 |
| net_avg_loss | -105.8154 |
| avg_hold_time_bars | 12.7363 |
| exposure | 0.3381 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
