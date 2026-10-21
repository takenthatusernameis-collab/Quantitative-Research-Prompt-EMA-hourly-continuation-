# EMA Hourly Continuation — EDU/USDT P50_144

**Symbol:** EDU/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.7238 |
| net_win_rate | 0.4843 |
| gross_profit_factor | 0.9095 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -1.8509 |
| sortino_ratio | -0.5353 |
| max_drawdown | 0.5250 |
| cagr | -0.2192 |
| net_avg_win | 60.8435 |
| net_avg_loss | -78.9282 |
| avg_hold_time_bars | 13.8208 |
| exposure | 0.2583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
