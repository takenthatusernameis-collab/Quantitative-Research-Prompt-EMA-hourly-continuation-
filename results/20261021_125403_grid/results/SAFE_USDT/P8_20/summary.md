# EMA Hourly Continuation — SAFE/USDT P8_20

**Symbol:** SAFE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.7042 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9679 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -2.8276 |
| sortino_ratio | -0.9547 |
| max_drawdown | 0.6699 |
| cagr | -0.3540 |
| net_avg_win | 58.9326 |
| net_avg_loss | -78.9740 |
| avg_hold_time_bars | 6.2772 |
| exposure | 0.1587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
