# EMA Hourly Continuation — G/USDT P34_200

**Symbol:** G/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.5056 |
| net_win_rate | 0.4259 |
| gross_profit_factor | 0.7240 |
| gross_win_rate | 0.4290 |
| sharpe_ratio | -3.8481 |
| sortino_ratio | -1.0222 |
| max_drawdown | 0.6881 |
| cagr | -0.3955 |
| net_avg_win | 50.3608 |
| net_avg_loss | -73.8795 |
| avg_hold_time_bars | 32.5237 |
| exposure | 0.5421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
