# EMA Hourly Continuation — BNB/USDT P8_200

**Symbol:** BNB/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.7075 |
| net_win_rate | 0.5116 |
| gross_profit_factor | 1.0221 |
| gross_win_rate | 0.5150 |
| sharpe_ratio | -1.6631 |
| sortino_ratio | -0.4129 |
| max_drawdown | 0.4044 |
| cagr | -0.1728 |
| net_avg_win | 59.5330 |
| net_avg_loss | -88.1490 |
| avg_hold_time_bars | 56.0997 |
| exposure | 0.7675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
