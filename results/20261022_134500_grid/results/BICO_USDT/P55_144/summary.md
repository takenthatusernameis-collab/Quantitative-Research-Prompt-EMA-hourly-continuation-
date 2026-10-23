# EMA Hourly Continuation — BICO/USDT P55_144

**Symbol:** BICO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.5916 |
| net_win_rate | 0.4442 |
| gross_profit_factor | 0.8427 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -3.5598 |
| sortino_ratio | -1.0732 |
| max_drawdown | 0.7280 |
| cagr | -0.3974 |
| net_avg_win | 51.3532 |
| net_avg_loss | -69.3778 |
| avg_hold_time_bars | 14.6455 |
| exposure | 0.3042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
