# EMA Hourly Continuation — IOTX/USDT P50_89

**Symbol:** IOTX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.4540 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.8306 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -6.8031 |
| sortino_ratio | -2.5672 |
| max_drawdown | 0.9607 |
| cagr | -0.7236 |
| net_avg_win | 24.9589 |
| net_avg_loss | -43.4348 |
| avg_hold_time_bars | 4.3848 |
| exposure | 0.1445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
