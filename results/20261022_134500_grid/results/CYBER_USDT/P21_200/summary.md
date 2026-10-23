# EMA Hourly Continuation — CYBER/USDT P21_200

**Symbol:** CYBER/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.7096 |
| net_win_rate | 0.4822 |
| gross_profit_factor | 0.9556 |
| gross_win_rate | 0.4849 |
| sharpe_ratio | -2.1576 |
| sortino_ratio | -0.5808 |
| max_drawdown | 0.5135 |
| cagr | -0.2413 |
| net_avg_win | 69.4511 |
| net_avg_loss | -91.1392 |
| avg_hold_time_bars | 38.9945 |
| exposure | 0.6470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
