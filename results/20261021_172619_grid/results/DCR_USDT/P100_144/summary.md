# EMA Hourly Continuation — DCR/USDT P100_144

**Symbol:** DCR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.5012 |
| net_win_rate | 0.4332 |
| gross_profit_factor | 0.7458 |
| gross_win_rate | 0.4332 |
| sharpe_ratio | -3.3648 |
| sortino_ratio | -0.7966 |
| max_drawdown | 0.6087 |
| cagr | -0.3083 |
| net_avg_win | 50.6955 |
| net_avg_loss | -77.3078 |
| avg_hold_time_bars | 6.5993 |
| exposure | 0.0827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
