# EMA Hourly Continuation — LSK/USDT P21_144

**Symbol:** LSK/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.7820 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 0.9904 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -1.4929 |
| sortino_ratio | -0.4229 |
| max_drawdown | 0.4430 |
| cagr | -0.1781 |
| net_avg_win | 71.1850 |
| net_avg_loss | -90.5682 |
| avg_hold_time_bars | 28.8270 |
| exposure | 0.5150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
