# EMA Hourly Continuation — XAI/USDT P89_144

**Symbol:** XAI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.6091 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9596 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -3.7606 |
| sortino_ratio | -1.1818 |
| max_drawdown | 0.7701 |
| cagr | -0.4331 |
| net_avg_win | 50.5768 |
| net_avg_loss | -74.4480 |
| avg_hold_time_bars | 6.0465 |
| exposure | 0.1360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
