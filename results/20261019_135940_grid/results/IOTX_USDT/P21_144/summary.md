# EMA Hourly Continuation — IOTX/USDT P21_144

**Symbol:** IOTX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 568 |
| net_profit_factor | 0.5919 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.8641 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -3.7117 |
| sortino_ratio | -1.2461 |
| max_drawdown | 0.7788 |
| cagr | -0.4471 |
| net_avg_win | 42.3788 |
| net_avg_loss | -62.6162 |
| avg_hold_time_bars | 19.1637 |
| exposure | 0.4948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
