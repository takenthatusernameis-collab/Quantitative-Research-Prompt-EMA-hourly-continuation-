# EMA Hourly Continuation — ENS/USDT P34_200

**Symbol:** ENS/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.5616 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8219 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -3.1391 |
| sortino_ratio | -0.8302 |
| max_drawdown | 0.6717 |
| cagr | -0.3351 |
| net_avg_win | 49.4834 |
| net_avg_loss | -74.6217 |
| avg_hold_time_bars | 33.8177 |
| exposure | 0.5565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
