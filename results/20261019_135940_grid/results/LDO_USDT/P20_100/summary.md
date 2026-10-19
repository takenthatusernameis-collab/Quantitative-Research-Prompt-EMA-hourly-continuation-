# EMA Hourly Continuation — LDO/USDT P20_100

**Symbol:** LDO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.5793 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.8200 |
| gross_win_rate | 0.4474 |
| sharpe_ratio | -4.6363 |
| sortino_ratio | -1.6507 |
| max_drawdown | 0.8663 |
| cagr | -0.5468 |
| net_avg_win | 41.5431 |
| net_avg_loss | -56.9749 |
| avg_hold_time_bars | 14.4164 |
| exposure | 0.4233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
