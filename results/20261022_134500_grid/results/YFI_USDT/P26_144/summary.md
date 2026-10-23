# EMA Hourly Continuation — YFI/USDT P26_144

**Symbol:** YFI/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.5852 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9972 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -3.8484 |
| sortino_ratio | -1.2243 |
| max_drawdown | 0.7875 |
| cagr | -0.4465 |
| net_avg_win | 44.2766 |
| net_avg_loss | -69.7286 |
| avg_hold_time_bars | 21.4913 |
| exposure | 0.5008 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
