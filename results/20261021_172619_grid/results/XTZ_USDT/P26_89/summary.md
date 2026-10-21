# EMA Hourly Continuation — XTZ/USDT P26_89

**Symbol:** XTZ/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.7099 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 0.9687 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -2.7060 |
| sortino_ratio | -0.8791 |
| max_drawdown | 0.6487 |
| cagr | -0.3315 |
| net_avg_win | 62.5309 |
| net_avg_loss | -82.4559 |
| avg_hold_time_bars | 13.8408 |
| exposure | 0.3240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
