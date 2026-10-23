# EMA Hourly Continuation — ENJ/USDT P34_89

**Symbol:** ENJ/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 710 |
| net_profit_factor | 0.6608 |
| net_win_rate | 0.4944 |
| gross_profit_factor | 1.0967 |
| gross_win_rate | 0.5113 |
| sharpe_ratio | -3.9493 |
| sortino_ratio | -1.4802 |
| max_drawdown | 0.8444 |
| cagr | -0.5083 |
| net_avg_win | 46.2356 |
| net_avg_loss | -68.4127 |
| avg_hold_time_bars | 7.7521 |
| exposure | 0.2491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
