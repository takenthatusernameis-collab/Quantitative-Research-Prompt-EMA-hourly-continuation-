# EMA Hourly Continuation — EDU/USDT P21_89

**Symbol:** EDU/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 778 |
| net_profit_factor | 0.6030 |
| net_win_rate | 0.4666 |
| gross_profit_factor | 0.8651 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -4.2026 |
| sortino_ratio | -1.6565 |
| max_drawdown | 0.8682 |
| cagr | -0.5414 |
| net_avg_win | 35.9848 |
| net_avg_loss | -52.2004 |
| avg_hold_time_bars | 10.6234 |
| exposure | 0.3740 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
