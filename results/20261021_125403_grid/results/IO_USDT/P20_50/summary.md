# EMA Hourly Continuation — IO/USDT P20_50

**Symbol:** IO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.7949 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9785 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -1.6683 |
| sortino_ratio | -0.5217 |
| max_drawdown | 0.4502 |
| cagr | -0.2143 |
| net_avg_win | 76.0641 |
| net_avg_loss | -92.7525 |
| avg_hold_time_bars | 7.9421 |
| exposure | 0.1726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
