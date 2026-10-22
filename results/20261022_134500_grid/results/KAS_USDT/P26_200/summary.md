# EMA Hourly Continuation — KAS/USDT P26_200

**Symbol:** KAS/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.5374 |
| net_win_rate | 0.4631 |
| gross_profit_factor | 0.8342 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -4.0157 |
| sortino_ratio | -1.2245 |
| max_drawdown | 0.7946 |
| cagr | -0.4597 |
| net_avg_win | 40.4479 |
| net_avg_loss | -64.9248 |
| avg_hold_time_bars | 21.4713 |
| exposure | 0.4763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
