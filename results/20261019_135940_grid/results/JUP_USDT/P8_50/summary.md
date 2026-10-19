# EMA Hourly Continuation — JUP/USDT P8_50

**Symbol:** JUP/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1103 |
| net_profit_factor | 0.6741 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 1.0206 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -5.1191 |
| sortino_ratio | -2.3780 |
| max_drawdown | 0.9472 |
| cagr | -0.6837 |
| net_avg_win | 36.9326 |
| net_avg_loss | -50.4914 |
| avg_hold_time_bars | 8.9130 |
| exposure | 0.4469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
