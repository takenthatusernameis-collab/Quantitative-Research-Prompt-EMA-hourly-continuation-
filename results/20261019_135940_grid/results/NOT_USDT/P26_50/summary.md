# EMA Hourly Continuation — NOT/USDT P26_50

**Symbol:** NOT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 978 |
| net_profit_factor | 0.5060 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.8629 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -7.6566 |
| sortino_ratio | -3.4265 |
| max_drawdown | 0.9846 |
| cagr | -0.8187 |
| net_avg_win | 23.0152 |
| net_avg_loss | -36.8945 |
| avg_hold_time_bars | 3.3303 |
| exposure | 0.1530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
