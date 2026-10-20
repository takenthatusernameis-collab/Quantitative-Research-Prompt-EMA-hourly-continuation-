# EMA Hourly Continuation — ZEN/USDT P12_100

**Symbol:** ZEN/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 616 |
| net_profit_factor | 0.5893 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.8768 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -3.6903 |
| sortino_ratio | -1.2881 |
| max_drawdown | 0.7872 |
| cagr | -0.4582 |
| net_avg_win | 39.4086 |
| net_avg_loss | -57.9548 |
| avg_hold_time_bars | 21.8815 |
| exposure | 0.6127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
