# EMA Hourly Continuation — EWT/USDT P50_144

**Symbol:** EWT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6699 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8196 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -2.2812 |
| sortino_ratio | -0.5931 |
| max_drawdown | 0.5379 |
| cagr | -0.2396 |
| net_avg_win | 66.3999 |
| net_avg_loss | -81.8781 |
| avg_hold_time_bars | 13.7738 |
| exposure | 0.2104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
