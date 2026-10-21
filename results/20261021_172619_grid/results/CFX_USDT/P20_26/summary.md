# EMA Hourly Continuation — CFX/USDT P20_26

**Symbol:** CFX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 168 |
| net_profit_factor | 0.6062 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.8669 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -2.0555 |
| sortino_ratio | -0.3815 |
| max_drawdown | 0.4083 |
| cagr | -0.1607 |
| net_avg_win | 70.2285 |
| net_avg_loss | -100.4078 |
| avg_hold_time_bars | 4.7798 |
| exposure | 0.0365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
