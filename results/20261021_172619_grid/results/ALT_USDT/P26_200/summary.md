# EMA Hourly Continuation — ALT/USDT P26_200

**Symbol:** ALT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.7563 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9040 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -1.5775 |
| sortino_ratio | -0.4083 |
| max_drawdown | 0.4130 |
| cagr | -0.1728 |
| net_avg_win | 74.4176 |
| net_avg_loss | -89.8687 |
| avg_hold_time_bars | 39.0846 |
| exposure | 0.5880 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
