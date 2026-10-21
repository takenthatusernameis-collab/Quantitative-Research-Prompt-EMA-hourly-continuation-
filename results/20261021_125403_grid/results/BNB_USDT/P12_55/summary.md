# EMA Hourly Continuation — BNB/USDT P12_55

**Symbol:** BNB/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.6152 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 1.0064 |
| gross_win_rate | 0.4903 |
| sharpe_ratio | -3.9952 |
| sortino_ratio | -1.3704 |
| max_drawdown | 0.8017 |
| cagr | -0.4678 |
| net_avg_win | 45.5521 |
| net_avg_loss | -71.2320 |
| avg_hold_time_bars | 12.8770 |
| exposure | 0.3330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
