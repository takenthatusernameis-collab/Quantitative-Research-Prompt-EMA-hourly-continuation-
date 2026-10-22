# EMA Hourly Continuation — CHR/USDT P34_89

**Symbol:** CHR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7420 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9456 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -2.3044 |
| sortino_ratio | -0.7398 |
| max_drawdown | 0.5922 |
| cagr | -0.2883 |
| net_avg_win | 67.9010 |
| net_avg_loss | -84.5729 |
| avg_hold_time_bars | 9.4035 |
| exposure | 0.2162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
