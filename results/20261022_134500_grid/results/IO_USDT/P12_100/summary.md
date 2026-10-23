# EMA Hourly Continuation — IO/USDT P12_100

**Symbol:** IO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.6538 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.9104 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -3.8906 |
| sortino_ratio | -1.4315 |
| max_drawdown | 0.8152 |
| cagr | -0.4959 |
| net_avg_win | 50.2661 |
| net_avg_loss | -67.4666 |
| avg_hold_time_bars | 18.1677 |
| exposure | 0.5664 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
