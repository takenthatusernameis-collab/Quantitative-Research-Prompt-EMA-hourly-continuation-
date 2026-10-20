# EMA Hourly Continuation — ACE/USDT P34_55

**Symbol:** ACE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 700 |
| net_profit_factor | 0.5296 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9940 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -4.8309 |
| sortino_ratio | -1.7991 |
| max_drawdown | 0.8896 |
| cagr | -0.5796 |
| net_avg_win | 29.0455 |
| net_avg_loss | -53.0005 |
| avg_hold_time_bars | 4.7929 |
| exposure | 0.1518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
