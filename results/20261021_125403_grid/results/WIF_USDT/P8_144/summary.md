# EMA Hourly Continuation — WIF/USDT P8_144

**Symbol:** WIF/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.7594 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.8640 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -1.6369 |
| sortino_ratio | -0.4399 |
| max_drawdown | 0.4318 |
| cagr | -0.1848 |
| net_avg_win | 75.8466 |
| net_avg_loss | -86.8758 |
| avg_hold_time_bars | 44.0780 |
| exposure | 0.7193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
