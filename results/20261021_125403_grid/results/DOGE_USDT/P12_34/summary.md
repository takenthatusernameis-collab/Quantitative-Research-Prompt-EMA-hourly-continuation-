# EMA Hourly Continuation — DOGE/USDT P12_34

**Symbol:** DOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.7313 |
| net_win_rate | 0.5055 |
| gross_profit_factor | 1.0091 |
| gross_win_rate | 0.5055 |
| sharpe_ratio | -2.2418 |
| sortino_ratio | -0.7556 |
| max_drawdown | 0.5856 |
| cagr | -0.2926 |
| net_avg_win | 56.8617 |
| net_avg_loss | -79.4697 |
| avg_hold_time_bars | 6.1618 |
| exposure | 0.1540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
