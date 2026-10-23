# EMA Hourly Continuation — UMA/USDT P34_89

**Symbol:** UMA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.5588 |
| net_win_rate | 0.4659 |
| gross_profit_factor | 0.9288 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -4.8035 |
| sortino_ratio | -1.7598 |
| max_drawdown | 0.8899 |
| cagr | -0.5709 |
| net_avg_win | 35.5184 |
| net_avg_loss | -55.4394 |
| avg_hold_time_bars | 8.5104 |
| exposure | 0.2607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
