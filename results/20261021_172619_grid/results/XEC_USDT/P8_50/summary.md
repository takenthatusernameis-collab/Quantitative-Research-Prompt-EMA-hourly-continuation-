# EMA Hourly Continuation — XEC/USDT P8_50

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 802 |
| net_profit_factor | 0.7320 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0018 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.8961 |
| sortino_ratio | -1.1734 |
| max_drawdown | 0.7605 |
| cagr | -0.4157 |
| net_avg_win | 50.5672 |
| net_avg_loss | -69.0768 |
| avg_hold_time_bars | 12.2419 |
| exposure | 0.4443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
