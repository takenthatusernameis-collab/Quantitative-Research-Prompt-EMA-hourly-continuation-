# EMA Hourly Continuation — IMX/USDT P21_26

**Symbol:** IMX/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1167 |
| net_profit_factor | 0.2361 |
| net_win_rate | 0.3796 |
| gross_profit_factor | 0.6695 |
| gross_win_rate | 0.4267 |
| sharpe_ratio | -13.1982 |
| sortino_ratio | -6.4739 |
| max_drawdown | 0.9998 |
| cagr | -0.9681 |
| net_avg_win | 6.9761 |
| net_avg_loss | -18.0784 |
| avg_hold_time_bars | 1.9229 |
| exposure | 0.1015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
