# EMA Hourly Continuation — AKT/USDT P34_55

**Symbol:** AKT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.9438 |
| net_win_rate | 0.5544 |
| gross_profit_factor | 1.2325 |
| gross_win_rate | 0.5544 |
| sharpe_ratio | -0.2517 |
| sortino_ratio | -0.0618 |
| max_drawdown | 0.1603 |
| cagr | -0.0318 |
| net_avg_win | 82.9580 |
| net_avg_loss | -109.3488 |
| avg_hold_time_bars | 6.3825 |
| exposure | 0.0827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
