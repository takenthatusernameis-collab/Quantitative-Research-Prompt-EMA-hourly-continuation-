# EMA Hourly Continuation — XRP/USDT P20_144

**Symbol:** XRP/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.7993 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0604 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -1.2813 |
| sortino_ratio | -0.3514 |
| max_drawdown | 0.3834 |
| cagr | -0.1493 |
| net_avg_win | 70.7234 |
| net_avg_loss | -94.5117 |
| avg_hold_time_bars | 30.5852 |
| exposure | 0.5060 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
