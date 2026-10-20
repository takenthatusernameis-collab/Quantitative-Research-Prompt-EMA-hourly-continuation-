# EMA Hourly Continuation — CFG/USDT P21_89

**Symbol:** CFG/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.5747 |
| net_win_rate | 0.4373 |
| gross_profit_factor | 0.8397 |
| gross_win_rate | 0.4422 |
| sharpe_ratio | -4.4212 |
| sortino_ratio | -1.5347 |
| max_drawdown | 0.8450 |
| cagr | -0.5151 |
| net_avg_win | 42.7073 |
| net_avg_loss | -57.7532 |
| avg_hold_time_bars | 18.0858 |
| exposure | 0.4982 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
