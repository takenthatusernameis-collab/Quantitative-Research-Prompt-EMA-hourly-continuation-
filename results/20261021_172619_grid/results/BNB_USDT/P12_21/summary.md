# EMA Hourly Continuation — BNB/USDT P12_21

**Symbol:** BNB/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.5796 |
| net_win_rate | 0.5020 |
| gross_profit_factor | 1.1101 |
| gross_win_rate | 0.5224 |
| sharpe_ratio | -2.6611 |
| sortino_ratio | -0.6048 |
| max_drawdown | 0.5109 |
| cagr | -0.2402 |
| net_avg_win | 55.8497 |
| net_avg_loss | -97.1566 |
| avg_hold_time_bars | 5.6286 |
| exposure | 0.0627 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
