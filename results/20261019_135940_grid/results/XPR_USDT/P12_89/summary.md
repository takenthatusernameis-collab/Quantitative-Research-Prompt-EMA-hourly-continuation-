# EMA Hourly Continuation — XPR/USDT P12_89

**Symbol:** XPR/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 878 |
| net_profit_factor | 0.4870 |
| net_win_rate | 0.4226 |
| gross_profit_factor | 0.8096 |
| gross_win_rate | 0.4294 |
| sharpe_ratio | -7.4578 |
| sortino_ratio | -3.0849 |
| max_drawdown | 0.9805 |
| cagr | -0.7865 |
| net_avg_win | 25.0624 |
| net_avg_loss | -37.6551 |
| avg_hold_time_bars | 10.4214 |
| exposure | 0.4159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
