# EMA Hourly Continuation — XMR/USDT P21_200

**Symbol:** XMR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.8154 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 1.0248 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -1.3772 |
| sortino_ratio | -0.3953 |
| max_drawdown | 0.4618 |
| cagr | -0.1668 |
| net_avg_win | 80.3807 |
| net_avg_loss | -99.5623 |
| avg_hold_time_bars | 29.5373 |
| exposure | 0.5397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
