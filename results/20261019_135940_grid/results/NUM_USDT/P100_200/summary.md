# EMA Hourly Continuation — NUM/USDT P100_200

**Symbol:** NUM/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.5493 |
| net_win_rate | 0.4239 |
| gross_profit_factor | 0.7905 |
| gross_win_rate | 0.4264 |
| sharpe_ratio | -4.0048 |
| sortino_ratio | -1.1198 |
| max_drawdown | 0.7502 |
| cagr | -0.4108 |
| net_avg_win | 53.6522 |
| net_avg_loss | -71.8540 |
| avg_hold_time_bars | 10.8985 |
| exposure | 0.1952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
