# EMA Hourly Continuation — BNB/USDT P20_21

**Symbol:** BNB/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 97 |
| net_profit_factor | 0.6611 |
| net_win_rate | 0.5567 |
| gross_profit_factor | 1.3117 |
| gross_win_rate | 0.5670 |
| sharpe_ratio | -1.2222 |
| sortino_ratio | -0.1752 |
| max_drawdown | 0.2070 |
| cagr | -0.0765 |
| net_avg_win | 65.4308 |
| net_avg_loss | -124.2868 |
| avg_hold_time_bars | 6.3196 |
| exposure | 0.0279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
