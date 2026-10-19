# EMA Hourly Continuation — TRX/USDT P20_200

**Symbol:** TRX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.4196 |
| net_win_rate | 0.4367 |
| gross_profit_factor | 0.9289 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -5.6358 |
| sortino_ratio | -1.5511 |
| max_drawdown | 0.8745 |
| cagr | -0.5591 |
| net_avg_win | 37.3118 |
| net_avg_loss | -68.9288 |
| avg_hold_time_bars | 34.2377 |
| exposure | 0.6023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
