# EMA Hourly Continuation — ALT/USDT P12_89

**Symbol:** ALT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.7089 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9680 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -2.8171 |
| sortino_ratio | -1.0378 |
| max_drawdown | 0.7241 |
| cagr | -0.3861 |
| net_avg_win | 51.8036 |
| net_avg_loss | -69.7196 |
| avg_hold_time_bars | 16.9868 |
| exposure | 0.5250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
