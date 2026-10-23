# EMA Hourly Continuation — MLK/USDT P20_89

**Symbol:** MLK/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1038 |
| net_profit_factor | 0.3451 |
| net_win_rate | 0.3044 |
| gross_profit_factor | 0.6039 |
| gross_win_rate | 0.3112 |
| sharpe_ratio | -12.6505 |
| sortino_ratio | -5.7936 |
| max_drawdown | 0.9994 |
| cagr | -0.9452 |
| net_avg_win | 16.6644 |
| net_avg_loss | -21.1348 |
| avg_hold_time_bars | 7.7457 |
| exposure | 0.3639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
