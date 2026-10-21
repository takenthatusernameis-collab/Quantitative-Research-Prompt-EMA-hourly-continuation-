# EMA Hourly Continuation — TAO/USDT P34_144

**Symbol:** TAO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.8599 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0158 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -0.8609 |
| sortino_ratio | -0.2304 |
| max_drawdown | 0.2701 |
| cagr | -0.1031 |
| net_avg_win | 83.3687 |
| net_avg_loss | -98.6294 |
| avg_hold_time_bars | 20.9713 |
| exposure | 0.3327 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
