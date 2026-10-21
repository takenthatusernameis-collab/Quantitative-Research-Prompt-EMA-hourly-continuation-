# EMA Hourly Continuation — IO/USDT P89_144

**Symbol:** IO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.7813 |
| net_win_rate | 0.4962 |
| gross_profit_factor | 0.9633 |
| gross_win_rate | 0.4962 |
| sharpe_ratio | -1.2014 |
| sortino_ratio | -0.2884 |
| max_drawdown | 0.3009 |
| cagr | -0.1250 |
| net_avg_win | 73.6303 |
| net_avg_loss | -92.8264 |
| avg_hold_time_bars | 8.0379 |
| exposure | 0.1027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
