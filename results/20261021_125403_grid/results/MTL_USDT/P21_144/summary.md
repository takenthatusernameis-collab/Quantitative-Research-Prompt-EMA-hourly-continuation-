# EMA Hourly Continuation — MTL/USDT P21_144

**Symbol:** MTL/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.7402 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9548 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -1.8368 |
| sortino_ratio | -0.5016 |
| max_drawdown | 0.4693 |
| cagr | -0.2068 |
| net_avg_win | 70.0409 |
| net_avg_loss | -90.6026 |
| avg_hold_time_bars | 33.5679 |
| exposure | 0.5590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
