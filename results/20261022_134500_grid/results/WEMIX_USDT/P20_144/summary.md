# EMA Hourly Continuation — WEMIX/USDT P20_144

**Symbol:** WEMIX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.3495 |
| net_win_rate | 0.3296 |
| gross_profit_factor | 0.5584 |
| gross_win_rate | 0.3423 |
| sharpe_ratio | -9.5384 |
| sortino_ratio | -3.6028 |
| max_drawdown | 0.9895 |
| cagr | -0.8362 |
| net_avg_win | 22.7172 |
| net_avg_loss | -31.9526 |
| avg_hold_time_bars | 18.9479 |
| exposure | 0.6115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
