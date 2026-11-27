# EMA Hourly Continuation — SHR/USDT P26_200

**Symbol:** SHR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.5561 |
| net_win_rate | 0.3900 |
| gross_profit_factor | 0.7042 |
| gross_win_rate | 0.3900 |
| sharpe_ratio | -5.4686 |
| sortino_ratio | -1.9908 |
| max_drawdown | 0.9141 |
| cagr | -0.6114 |
| net_avg_win | 42.7618 |
| net_avg_loss | -49.1659 |
| avg_hold_time_bars | 15.2185 |
| exposure | 0.4697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
