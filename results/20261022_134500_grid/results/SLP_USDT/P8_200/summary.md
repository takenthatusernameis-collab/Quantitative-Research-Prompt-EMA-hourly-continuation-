# EMA Hourly Continuation — SLP/USDT P8_200

**Symbol:** SLP/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.5919 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.8589 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -3.9712 |
| sortino_ratio | -1.2238 |
| max_drawdown | 0.7823 |
| cagr | -0.4457 |
| net_avg_win | 52.1247 |
| net_avg_loss | -70.1268 |
| avg_hold_time_bars | 35.2557 |
| exposure | 0.7772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
