# EMA Hourly Continuation — ALT/USDT P34_89

**Symbol:** ALT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.6211 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.9179 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -3.7538 |
| sortino_ratio | -1.3589 |
| max_drawdown | 0.8054 |
| cagr | -0.4734 |
| net_avg_win | 42.1707 |
| net_avg_loss | -61.0331 |
| avg_hold_time_bars | 8.6180 |
| exposure | 0.2574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
