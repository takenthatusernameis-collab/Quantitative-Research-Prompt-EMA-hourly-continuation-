# EMA Hourly Continuation — AXS/USDT P8_34

**Symbol:** AXS/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.8143 |
| net_win_rate | 0.5196 |
| gross_profit_factor | 1.0939 |
| gross_win_rate | 0.5196 |
| sharpe_ratio | -1.8605 |
| sortino_ratio | -0.7155 |
| max_drawdown | 0.5843 |
| cagr | -0.2803 |
| net_avg_win | 66.4422 |
| net_avg_loss | -88.2393 |
| avg_hold_time_bars | 9.1061 |
| exposure | 0.2950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
