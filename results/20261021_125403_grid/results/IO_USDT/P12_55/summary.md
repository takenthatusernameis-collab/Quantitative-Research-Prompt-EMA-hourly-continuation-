# EMA Hourly Continuation — IO/USDT P12_55

**Symbol:** IO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 566 |
| net_profit_factor | 0.8264 |
| net_win_rate | 0.4982 |
| gross_profit_factor | 0.9910 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -1.4878 |
| sortino_ratio | -0.5229 |
| max_drawdown | 0.4859 |
| cagr | -0.2156 |
| net_avg_win | 73.6004 |
| net_avg_loss | -88.4345 |
| avg_hold_time_bars | 12.5088 |
| exposure | 0.3428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
