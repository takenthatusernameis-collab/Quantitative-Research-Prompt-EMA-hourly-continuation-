# EMA Hourly Continuation — GMX/USDT P26_89

**Symbol:** GMX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.5439 |
| net_win_rate | 0.4386 |
| gross_profit_factor | 0.8649 |
| gross_win_rate | 0.4441 |
| sharpe_ratio | -5.6896 |
| sortino_ratio | -2.1588 |
| max_drawdown | 0.9280 |
| cagr | -0.6427 |
| net_avg_win | 34.6750 |
| net_avg_loss | -49.8097 |
| avg_hold_time_bars | 9.1890 |
| exposure | 0.3028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
