# EMA Hourly Continuation — RPL/USDT P21_89

**Symbol:** RPL/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.6203 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.9115 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -3.8270 |
| sortino_ratio | -1.4189 |
| max_drawdown | 0.8172 |
| cagr | -0.4850 |
| net_avg_win | 41.0920 |
| net_avg_loss | -58.6227 |
| avg_hold_time_bars | 13.0000 |
| exposure | 0.4048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
