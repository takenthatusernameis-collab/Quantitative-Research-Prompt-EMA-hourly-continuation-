# EMA Hourly Continuation — CRV/USDT P100_144

**Symbol:** CRV/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.6695 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.8842 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -1.9158 |
| sortino_ratio | -0.4272 |
| max_drawdown | 0.3927 |
| cagr | -0.1776 |
| net_avg_win | 68.3423 |
| net_avg_loss | -91.0007 |
| avg_hold_time_bars | 5.9426 |
| exposure | 0.0659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
