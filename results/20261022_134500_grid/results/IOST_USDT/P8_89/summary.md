# EMA Hourly Continuation — IOST/USDT P8_89

**Symbol:** IOST/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.6702 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0457 |
| gross_win_rate | 0.5108 |
| sharpe_ratio | -3.1698 |
| sortino_ratio | -1.1302 |
| max_drawdown | 0.7618 |
| cagr | -0.4232 |
| net_avg_win | 46.9672 |
| net_avg_loss | -70.0809 |
| avg_hold_time_bars | 22.6034 |
| exposure | 0.6658 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
