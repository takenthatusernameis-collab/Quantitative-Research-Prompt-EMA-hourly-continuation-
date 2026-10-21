# EMA Hourly Continuation — UMA/USDT P89_200

**Symbol:** UMA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.6602 |
| net_win_rate | 0.4660 |
| gross_profit_factor | 0.8618 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -2.2247 |
| sortino_ratio | -0.5432 |
| max_drawdown | 0.4790 |
| cagr | -0.2208 |
| net_avg_win | 66.0129 |
| net_avg_loss | -87.2530 |
| avg_hold_time_bars | 15.0442 |
| exposure | 0.2010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
