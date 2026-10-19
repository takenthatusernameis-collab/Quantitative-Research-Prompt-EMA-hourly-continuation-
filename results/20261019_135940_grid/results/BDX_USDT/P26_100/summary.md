# EMA Hourly Continuation — BDX/USDT P26_100

**Symbol:** BDX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1219 |
| net_profit_factor | 0.3061 |
| net_win_rate | 0.3043 |
| gross_profit_factor | 0.6940 |
| gross_win_rate | 0.3536 |
| sharpe_ratio | -16.8105 |
| sortino_ratio | -8.7039 |
| max_drawdown | 1.0000 |
| cagr | -0.9917 |
| net_avg_win | 11.8876 |
| net_avg_loss | -16.9932 |
| avg_hold_time_bars | 4.8515 |
| exposure | 0.2688 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
