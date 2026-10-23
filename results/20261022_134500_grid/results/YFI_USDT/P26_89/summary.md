# EMA Hourly Continuation — YFI/USDT P26_89

**Symbol:** YFI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 814 |
| net_profit_factor | 0.4761 |
| net_win_rate | 0.4238 |
| gross_profit_factor | 0.9452 |
| gross_win_rate | 0.4533 |
| sharpe_ratio | -7.5919 |
| sortino_ratio | -3.0395 |
| max_drawdown | 0.9792 |
| cagr | -0.7802 |
| net_avg_win | 25.7679 |
| net_avg_loss | -39.8105 |
| avg_hold_time_bars | 8.1941 |
| exposure | 0.3018 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
