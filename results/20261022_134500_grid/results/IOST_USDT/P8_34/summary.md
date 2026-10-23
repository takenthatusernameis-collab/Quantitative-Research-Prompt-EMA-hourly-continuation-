# EMA Hourly Continuation — IOST/USDT P8_34

**Symbol:** IOST/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1298 |
| net_profit_factor | 0.4813 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.9521 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -7.8336 |
| sortino_ratio | -3.9553 |
| max_drawdown | 0.9929 |
| cagr | -0.8587 |
| net_avg_win | 15.2740 |
| net_avg_loss | -27.5351 |
| avg_hold_time_bars | 6.1926 |
| exposure | 0.3654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
