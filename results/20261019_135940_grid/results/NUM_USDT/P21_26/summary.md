# EMA Hourly Continuation — NUM/USDT P21_26

**Symbol:** NUM/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1096 |
| net_profit_factor | 0.1747 |
| net_win_rate | 0.2810 |
| gross_profit_factor | 0.6291 |
| gross_win_rate | 0.3285 |
| sharpe_ratio | -16.0504 |
| sortino_ratio | -7.8285 |
| max_drawdown | 1.0000 |
| cagr | -0.9847 |
| net_avg_win | 6.8703 |
| net_avg_loss | -15.3753 |
| avg_hold_time_bars | 2.9151 |
| exposure | 0.1452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
