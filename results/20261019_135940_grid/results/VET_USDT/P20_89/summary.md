# EMA Hourly Continuation — VET/USDT P20_89

**Symbol:** VET/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.6772 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.1062 |
| gross_win_rate | 0.5202 |
| sharpe_ratio | -3.6952 |
| sortino_ratio | -1.3914 |
| max_drawdown | 0.8309 |
| cagr | -0.4905 |
| net_avg_win | 47.0380 |
| net_avg_loss | -71.2189 |
| avg_hold_time_bars | 11.8581 |
| exposure | 0.3875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
