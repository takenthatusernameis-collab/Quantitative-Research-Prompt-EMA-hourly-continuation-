# EMA Hourly Continuation — COMP/USDT P20_26

**Symbol:** COMP/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1328 |
| net_profit_factor | 0.1813 |
| net_win_rate | 0.3697 |
| gross_profit_factor | 0.6889 |
| gross_win_rate | 0.4465 |
| sharpe_ratio | -14.9747 |
| sortino_ratio | -7.9207 |
| max_drawdown | 1.0000 |
| cagr | -0.9852 |
| net_avg_win | 4.5092 |
| net_avg_loss | -14.5923 |
| avg_hold_time_bars | 2.0361 |
| exposure | 0.1229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
