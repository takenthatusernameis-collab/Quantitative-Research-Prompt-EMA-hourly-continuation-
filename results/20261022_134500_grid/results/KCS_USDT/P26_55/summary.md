# EMA Hourly Continuation — KCS/USDT P26_55

**Symbol:** KCS/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 954 |
| net_profit_factor | 0.1814 |
| net_win_rate | 0.3061 |
| gross_profit_factor | 0.6576 |
| gross_win_rate | 0.3826 |
| sharpe_ratio | -14.7301 |
| sortino_ratio | -6.7715 |
| max_drawdown | 0.9999 |
| cagr | -0.9733 |
| net_avg_win | 7.5888 |
| net_avg_loss | -18.4514 |
| avg_hold_time_bars | 4.3333 |
| exposure | 0.1879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
