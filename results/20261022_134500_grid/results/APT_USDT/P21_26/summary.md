# EMA Hourly Continuation — APT/USDT P21_26

**Symbol:** APT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1237 |
| net_profit_factor | 0.1621 |
| net_win_rate | 0.3339 |
| gross_profit_factor | 0.6430 |
| gross_win_rate | 0.3808 |
| sharpe_ratio | -16.0024 |
| sortino_ratio | -8.2766 |
| max_drawdown | 1.0000 |
| cagr | -0.9891 |
| net_avg_win | 4.6859 |
| net_avg_loss | -14.4844 |
| avg_hold_time_bars | 1.7745 |
| exposure | 0.0998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
