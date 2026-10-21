# EMA Hourly Continuation — TIA/USDT P12_26

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.8226 |
| net_win_rate | 0.5228 |
| gross_profit_factor | 1.0664 |
| gross_win_rate | 0.5228 |
| sharpe_ratio | -1.1039 |
| sortino_ratio | -0.3250 |
| max_drawdown | 0.3960 |
| cagr | -0.1403 |
| net_avg_win | 67.2013 |
| net_avg_loss | -89.4917 |
| avg_hold_time_bars | 5.5731 |
| exposure | 0.1056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
