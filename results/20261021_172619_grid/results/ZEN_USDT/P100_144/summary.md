# EMA Hourly Continuation — ZEN/USDT P100_144

**Symbol:** ZEN/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.5887 |
| net_win_rate | 0.4415 |
| gross_profit_factor | 0.8046 |
| gross_win_rate | 0.4415 |
| sharpe_ratio | -2.7582 |
| sortino_ratio | -0.6391 |
| max_drawdown | 0.5351 |
| cagr | -0.2557 |
| net_avg_win | 64.0518 |
| net_avg_loss | -86.0178 |
| avg_hold_time_bars | 6.2642 |
| exposure | 0.0755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
