# EMA Hourly Continuation — KNC/USDT P20_26

**Symbol:** KNC/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.5125 |
| net_win_rate | 0.4424 |
| gross_profit_factor | 0.8643 |
| gross_win_rate | 0.4450 |
| sharpe_ratio | -4.5885 |
| sortino_ratio | -1.2907 |
| max_drawdown | 0.7816 |
| cagr | -0.4526 |
| net_avg_win | 48.5166 |
| net_avg_loss | -75.1051 |
| avg_hold_time_bars | 5.6911 |
| exposure | 0.0988 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
