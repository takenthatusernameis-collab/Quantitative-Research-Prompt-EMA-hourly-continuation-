# EMA Hourly Continuation — MNT/USDT P21_144

**Symbol:** MNT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.9013 |
| net_win_rate | 0.5373 |
| gross_profit_factor | 1.1413 |
| gross_win_rate | 0.5373 |
| sharpe_ratio | -0.5068 |
| sortino_ratio | -0.1336 |
| max_drawdown | 0.2618 |
| cagr | -0.0633 |
| net_avg_win | 76.8146 |
| net_avg_loss | -98.9729 |
| avg_hold_time_bars | 36.5701 |
| exposure | 0.5569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
