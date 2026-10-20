# EMA Hourly Continuation — BICO/USDT P12_55

**Symbol:** BICO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 921 |
| net_profit_factor | 0.5995 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.9280 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -4.4946 |
| sortino_ratio | -1.9283 |
| max_drawdown | 0.8992 |
| cagr | -0.5973 |
| net_avg_win | 30.4792 |
| net_avg_loss | -46.7140 |
| avg_hold_time_bars | 9.8046 |
| exposure | 0.4105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
