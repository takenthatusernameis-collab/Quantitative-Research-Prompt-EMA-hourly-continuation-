# EMA Hourly Continuation — BDX/USDT P34_100

**Symbol:** BDX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1174 |
| net_profit_factor | 0.2644 |
| net_win_rate | 0.2905 |
| gross_profit_factor | 0.6342 |
| gross_win_rate | 0.3467 |
| sharpe_ratio | -17.0583 |
| sortino_ratio | -8.7537 |
| max_drawdown | 1.0000 |
| cagr | -0.9917 |
| net_avg_win | 10.5417 |
| net_avg_loss | -16.3201 |
| avg_hold_time_bars | 4.2888 |
| exposure | 0.2289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
