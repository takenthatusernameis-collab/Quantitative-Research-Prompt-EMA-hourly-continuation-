# EMA Hourly Continuation — TIA/USDT P34_100

**Symbol:** TIA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.9203 |
| net_win_rate | 0.5276 |
| gross_profit_factor | 1.1142 |
| gross_win_rate | 0.5276 |
| sharpe_ratio | -0.5113 |
| sortino_ratio | -0.1471 |
| max_drawdown | 0.2719 |
| cagr | -0.0698 |
| net_avg_win | 91.3333 |
| net_avg_loss | -110.8574 |
| avg_hold_time_bars | 16.0251 |
| exposure | 0.2899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
