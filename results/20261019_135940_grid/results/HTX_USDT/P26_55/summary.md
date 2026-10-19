# EMA Hourly Continuation — HTX/USDT P26_55

**Symbol:** HTX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1021 |
| net_profit_factor | 0.1837 |
| net_win_rate | 0.2762 |
| gross_profit_factor | 0.6275 |
| gross_win_rate | 0.3575 |
| sharpe_ratio | -16.4315 |
| sortino_ratio | -7.9681 |
| max_drawdown | 1.0000 |
| cagr | -0.9873 |
| net_avg_win | 7.9804 |
| net_avg_loss | -16.5769 |
| avg_hold_time_bars | 4.9726 |
| exposure | 0.2297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
