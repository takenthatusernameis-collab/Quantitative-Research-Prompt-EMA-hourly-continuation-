# EMA Hourly Continuation — ONE/USDT P8_50

**Symbol:** ONE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1043 |
| net_profit_factor | 0.5628 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 0.8577 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -6.5432 |
| sortino_ratio | -2.9653 |
| max_drawdown | 0.9748 |
| cagr | -0.7618 |
| net_avg_win | 26.9267 |
| net_avg_loss | -38.4922 |
| avg_hold_time_bars | 10.4391 |
| exposure | 0.4949 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
