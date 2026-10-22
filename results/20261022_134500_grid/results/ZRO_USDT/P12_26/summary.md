# EMA Hourly Continuation — ZRO/USDT P12_26

**Symbol:** ZRO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1347 |
| net_profit_factor | 0.4964 |
| net_win_rate | 0.4454 |
| gross_profit_factor | 0.8981 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -9.5360 |
| sortino_ratio | -5.0913 |
| max_drawdown | 0.9974 |
| cagr | -0.9220 |
| net_avg_win | 16.3830 |
| net_avg_loss | -26.5110 |
| avg_hold_time_bars | 2.7350 |
| exposure | 0.1803 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
