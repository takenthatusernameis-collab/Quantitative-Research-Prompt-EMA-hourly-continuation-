# EMA Hourly Continuation — DBR/USDT P8_21

**Symbol:** DBR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1019 |
| net_profit_factor | 0.4795 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 1.0440 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -10.1994 |
| sortino_ratio | -5.1439 |
| max_drawdown | 0.9944 |
| cagr | -0.9248 |
| net_avg_win | 20.7262 |
| net_avg_loss | -33.1116 |
| avg_hold_time_bars | 4.5005 |
| exposure | 0.2608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
