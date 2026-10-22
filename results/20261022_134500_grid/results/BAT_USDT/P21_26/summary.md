# EMA Hourly Continuation — BAT/USDT P21_26

**Symbol:** BAT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1177 |
| net_profit_factor | 0.1353 |
| net_win_rate | 0.3619 |
| gross_profit_factor | 0.5970 |
| gross_win_rate | 0.4393 |
| sharpe_ratio | -14.3058 |
| sortino_ratio | -7.1647 |
| max_drawdown | 0.9999 |
| cagr | -0.9773 |
| net_avg_win | 3.6721 |
| net_avg_loss | -15.3976 |
| avg_hold_time_bars | 2.2523 |
| exposure | 0.1205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
