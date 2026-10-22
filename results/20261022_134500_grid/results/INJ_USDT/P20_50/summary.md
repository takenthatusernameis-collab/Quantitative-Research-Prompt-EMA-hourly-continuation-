# EMA Hourly Continuation — INJ/USDT P20_50

**Symbol:** INJ/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1002 |
| net_profit_factor | 0.5580 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9385 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -5.9423 |
| sortino_ratio | -2.6462 |
| max_drawdown | 0.9618 |
| cagr | -0.7245 |
| net_avg_win | 25.2634 |
| net_avg_loss | -41.6358 |
| avg_hold_time_bars | 4.4731 |
| exposure | 0.2037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
