# EMA Hourly Continuation — WIF/USDT P34_50

**Symbol:** WIF/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 213 |
| net_profit_factor | 0.9471 |
| net_win_rate | 0.5493 |
| gross_profit_factor | 1.2067 |
| gross_win_rate | 0.5493 |
| sharpe_ratio | -0.2229 |
| sortino_ratio | -0.0473 |
| max_drawdown | 0.2852 |
| cagr | -0.0244 |
| net_avg_win | 91.8451 |
| net_avg_loss | -118.1943 |
| avg_hold_time_bars | 5.6056 |
| exposure | 0.0543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
