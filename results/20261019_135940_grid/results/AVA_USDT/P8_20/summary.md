# EMA Hourly Continuation — AVA/USDT P8_20

**Symbol:** AVA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1578 |
| net_profit_factor | 0.3278 |
| net_win_rate | 0.4151 |
| gross_profit_factor | 0.8054 |
| gross_win_rate | 0.4373 |
| sharpe_ratio | -12.6776 |
| sortino_ratio | -7.1244 |
| max_drawdown | 0.9999 |
| cagr | -0.9742 |
| net_avg_win | 7.4442 |
| net_avg_loss | -16.1158 |
| avg_hold_time_bars | 2.8492 |
| exposure | 0.2044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
