# EMA Hourly Continuation — ACE/USDT P26_55

**Symbol:** ACE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 728 |
| net_profit_factor | 0.5933 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 1.0062 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -4.1200 |
| sortino_ratio | -1.5686 |
| max_drawdown | 0.8499 |
| cagr | -0.5241 |
| net_avg_win | 34.1120 |
| net_avg_loss | -56.8643 |
| avg_hold_time_bars | 6.0563 |
| exposure | 0.1995 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
