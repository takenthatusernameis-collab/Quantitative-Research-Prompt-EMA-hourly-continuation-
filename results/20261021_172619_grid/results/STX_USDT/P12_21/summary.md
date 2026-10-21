# EMA Hourly Continuation — STX/USDT P12_21

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.7389 |
| net_win_rate | 0.5083 |
| gross_profit_factor | 1.0289 |
| gross_win_rate | 0.5083 |
| sharpe_ratio | -1.6646 |
| sortino_ratio | -0.4156 |
| max_drawdown | 0.4412 |
| cagr | -0.1737 |
| net_avg_win | 70.1922 |
| net_avg_loss | -98.1830 |
| avg_hold_time_bars | 5.0759 |
| exposure | 0.0696 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
