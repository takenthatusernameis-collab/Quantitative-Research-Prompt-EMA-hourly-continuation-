# EMA Hourly Continuation — SSV/USDT P20_89

**Symbol:** SSV/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.7280 |
| net_win_rate | 0.4656 |
| gross_profit_factor | 0.8992 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -2.6129 |
| sortino_ratio | -0.8708 |
| max_drawdown | 0.6710 |
| cagr | -0.3303 |
| net_avg_win | 66.2431 |
| net_avg_loss | -79.2774 |
| avg_hold_time_bars | 14.5924 |
| exposure | 0.3645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
