# EMA Hourly Continuation — YGG/USDT P34_89

**Symbol:** YGG/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7287 |
| net_win_rate | 0.4823 |
| gross_profit_factor | 0.9269 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -2.1870 |
| sortino_ratio | -0.6818 |
| max_drawdown | 0.5629 |
| cagr | -0.2689 |
| net_avg_win | 63.5190 |
| net_avg_loss | -81.1876 |
| avg_hold_time_bars | 11.1148 |
| exposure | 0.2409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
