# EMA Hourly Continuation — XLM/USDT P26_144

**Symbol:** XLM/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.7318 |
| net_win_rate | 0.4957 |
| gross_profit_factor | 0.9583 |
| gross_win_rate | 0.4957 |
| sharpe_ratio | -1.6575 |
| sortino_ratio | -0.4401 |
| max_drawdown | 0.4267 |
| cagr | -0.1832 |
| net_avg_win | 63.5534 |
| net_avg_loss | -85.3508 |
| avg_hold_time_bars | 30.4928 |
| exposure | 0.4782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
