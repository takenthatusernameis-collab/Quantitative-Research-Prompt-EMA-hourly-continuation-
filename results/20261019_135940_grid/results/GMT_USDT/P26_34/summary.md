# EMA Hourly Continuation — GMT/USDT P26_34

**Symbol:** GMT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1098 |
| net_profit_factor | 0.2932 |
| net_win_rate | 0.3679 |
| gross_profit_factor | 0.8885 |
| gross_win_rate | 0.4080 |
| sharpe_ratio | -13.2521 |
| sortino_ratio | -6.3794 |
| max_drawdown | 0.9998 |
| cagr | -0.9645 |
| net_avg_win | 10.2677 |
| net_avg_loss | -20.3831 |
| avg_hold_time_bars | 2.0993 |
| exposure | 0.1048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
