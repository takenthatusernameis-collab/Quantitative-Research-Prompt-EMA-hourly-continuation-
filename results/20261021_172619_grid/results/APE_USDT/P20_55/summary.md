# EMA Hourly Continuation — APE/USDT P20_55

**Symbol:** APE/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.7496 |
| net_win_rate | 0.4960 |
| gross_profit_factor | 0.9883 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -2.0640 |
| sortino_ratio | -0.6614 |
| max_drawdown | 0.5413 |
| cagr | -0.2617 |
| net_avg_win | 64.3708 |
| net_avg_loss | -84.5066 |
| avg_hold_time_bars | 7.4340 |
| exposure | 0.1690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
