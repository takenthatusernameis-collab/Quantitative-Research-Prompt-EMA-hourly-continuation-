# EMA Hourly Continuation — LTC/USDT P55_200

**Symbol:** LTC/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.4079 |
| net_win_rate | 0.4238 |
| gross_profit_factor | 0.7729 |
| gross_win_rate | 0.4507 |
| sharpe_ratio | -5.3119 |
| sortino_ratio | -1.5721 |
| max_drawdown | 0.8649 |
| cagr | -0.5417 |
| net_avg_win | 31.3085 |
| net_avg_loss | -56.4522 |
| avg_hold_time_bars | 17.5135 |
| exposure | 0.3550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
