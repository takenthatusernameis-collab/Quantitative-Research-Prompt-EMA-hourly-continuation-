# EMA Hourly Continuation — AXS/USDT P21_26

**Symbol:** AXS/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1126 |
| net_profit_factor | 0.1618 |
| net_win_rate | 0.3508 |
| gross_profit_factor | 0.5580 |
| gross_win_rate | 0.4076 |
| sharpe_ratio | -14.8004 |
| sortino_ratio | -7.3210 |
| max_drawdown | 1.0000 |
| cagr | -0.9807 |
| net_avg_win | 4.8879 |
| net_avg_loss | -16.3204 |
| avg_hold_time_bars | 1.8526 |
| exposure | 0.0944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
