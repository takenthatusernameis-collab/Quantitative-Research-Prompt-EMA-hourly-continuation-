# EMA Hourly Continuation — DBR/USDT P8_55

**Symbol:** DBR/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.6000 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.9726 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -5.5737 |
| sortino_ratio | -2.3547 |
| max_drawdown | 0.9010 |
| cagr | -0.6718 |
| net_avg_win | 40.5921 |
| net_avg_loss | -58.1427 |
| avg_hold_time_bars | 11.7465 |
| exposure | 0.4769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
