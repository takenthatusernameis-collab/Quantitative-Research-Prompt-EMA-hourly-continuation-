# EMA Hourly Continuation — ZK/USDT P21_89

**Symbol:** ZK/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.8065 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9851 |
| gross_win_rate | 0.4930 |
| sharpe_ratio | -1.6766 |
| sortino_ratio | -0.5532 |
| max_drawdown | 0.5067 |
| cagr | -0.2261 |
| net_avg_win | 76.7825 |
| net_avg_loss | -92.5596 |
| avg_hold_time_bars | 14.4286 |
| exposure | 0.3496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
