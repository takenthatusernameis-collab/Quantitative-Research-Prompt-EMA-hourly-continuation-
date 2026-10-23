# EMA Hourly Continuation — LUNA/USDT P34_100

**Symbol:** LUNA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 784 |
| net_profit_factor | 0.4345 |
| net_win_rate | 0.4184 |
| gross_profit_factor | 0.7872 |
| gross_win_rate | 0.4311 |
| sharpe_ratio | -7.7112 |
| sortino_ratio | -3.0241 |
| max_drawdown | 0.9790 |
| cagr | -0.7836 |
| net_avg_win | 22.9251 |
| net_avg_loss | -37.9502 |
| avg_hold_time_bars | 7.0561 |
| exposure | 0.2515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
