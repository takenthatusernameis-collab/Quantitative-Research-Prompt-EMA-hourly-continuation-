# EMA Hourly Continuation — ALT/USDT P21_200

**Symbol:** ALT/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.7439 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.8808 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -1.6321 |
| sortino_ratio | -0.4148 |
| max_drawdown | 0.4170 |
| cagr | -0.1749 |
| net_avg_win | 73.6622 |
| net_avg_loss | -88.4791 |
| avg_hold_time_bars | 43.7062 |
| exposure | 0.6357 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
