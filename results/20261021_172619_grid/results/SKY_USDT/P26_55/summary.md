# EMA Hourly Continuation — SKY/USDT P26_55

**Symbol:** SKY/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.5886 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 0.8425 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -3.6115 |
| sortino_ratio | -1.1686 |
| max_drawdown | 0.6751 |
| cagr | -0.4153 |
| net_avg_win | 49.1629 |
| net_avg_loss | -72.0199 |
| avg_hold_time_bars | 7.6683 |
| exposure | 0.1792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
