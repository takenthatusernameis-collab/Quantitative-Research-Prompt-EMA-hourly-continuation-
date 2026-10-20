# EMA Hourly Continuation — ALT/USDT P34_55

**Symbol:** ALT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 786 |
| net_profit_factor | 0.4585 |
| net_win_rate | 0.4364 |
| gross_profit_factor | 0.8278 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -6.6828 |
| sortino_ratio | -2.6494 |
| max_drawdown | 0.9616 |
| cagr | -0.7235 |
| net_avg_win | 23.7083 |
| net_avg_loss | -40.0354 |
| avg_hold_time_bars | 4.6069 |
| exposure | 0.1646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
