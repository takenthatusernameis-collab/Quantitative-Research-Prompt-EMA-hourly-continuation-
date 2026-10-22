# EMA Hourly Continuation — ETH/USDT P8_144

**Symbol:** ETH/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.5153 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.9557 |
| gross_win_rate | 0.4958 |
| sharpe_ratio | -3.8360 |
| sortino_ratio | -1.0042 |
| max_drawdown | 0.7293 |
| cagr | -0.3972 |
| net_avg_win | 46.3663 |
| net_avg_loss | -77.3199 |
| avg_hold_time_bars | 48.9440 |
| exposure | 0.7942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
