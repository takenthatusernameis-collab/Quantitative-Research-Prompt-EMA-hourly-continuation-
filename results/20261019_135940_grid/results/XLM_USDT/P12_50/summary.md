# EMA Hourly Continuation — XLM/USDT P12_50

**Symbol:** XLM/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1128 |
| net_profit_factor | 0.3563 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8038 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -8.0557 |
| sortino_ratio | -3.7917 |
| max_drawdown | 0.9915 |
| cagr | -0.8494 |
| net_avg_win | 10.6743 |
| net_avg_loss | -25.0820 |
| avg_hold_time_bars | 6.9397 |
| exposure | 0.3558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
