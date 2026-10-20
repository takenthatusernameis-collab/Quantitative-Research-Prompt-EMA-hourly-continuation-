# EMA Hourly Continuation — ZETA/USDT P34_55

**Symbol:** ZETA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 911 |
| net_profit_factor | 0.4647 |
| net_win_rate | 0.4292 |
| gross_profit_factor | 0.8618 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -8.1630 |
| sortino_ratio | -3.4713 |
| max_drawdown | 0.9871 |
| cagr | -0.8213 |
| net_avg_win | 21.9107 |
| net_avg_loss | -35.4561 |
| avg_hold_time_bars | 3.4369 |
| exposure | 0.1417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
