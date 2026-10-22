# EMA Hourly Continuation — XMR/USDT P12_89

**Symbol:** XMR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1083 |
| net_profit_factor | 0.4067 |
| net_win_rate | 0.4312 |
| gross_profit_factor | 0.7730 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -8.4182 |
| sortino_ratio | -3.8722 |
| max_drawdown | 0.9926 |
| cagr | -0.8578 |
| net_avg_win | 14.5680 |
| net_avg_loss | -27.1568 |
| avg_hold_time_bars | 9.2632 |
| exposure | 0.4560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
