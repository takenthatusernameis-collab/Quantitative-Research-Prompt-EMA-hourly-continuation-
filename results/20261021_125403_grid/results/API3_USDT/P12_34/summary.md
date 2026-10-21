# EMA Hourly Continuation — API3/USDT P12_34

**Symbol:** API3/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 622 |
| net_profit_factor | 0.6441 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.8542 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -3.7872 |
| sortino_ratio | -1.3451 |
| max_drawdown | 0.7882 |
| cagr | -0.4610 |
| net_avg_win | 50.4074 |
| net_avg_loss | -65.3314 |
| avg_hold_time_bars | 7.7347 |
| exposure | 0.2187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
