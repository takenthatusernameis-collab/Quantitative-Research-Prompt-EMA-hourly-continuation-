# EMA Hourly Continuation — CYBER/USDT P12_50

**Symbol:** CYBER/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1021 |
| net_profit_factor | 0.5972 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.9586 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -6.0705 |
| sortino_ratio | -2.7195 |
| max_drawdown | 0.9653 |
| cagr | -0.7357 |
| net_avg_win | 30.1746 |
| net_avg_loss | -43.7826 |
| avg_hold_time_bars | 7.9618 |
| exposure | 0.3695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
