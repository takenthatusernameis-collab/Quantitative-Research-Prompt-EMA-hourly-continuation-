# EMA Hourly Continuation — ENS/USDT P21_34

**Symbol:** ENS/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1191 |
| net_profit_factor | 0.4192 |
| net_win_rate | 0.4022 |
| gross_profit_factor | 0.8763 |
| gross_win_rate | 0.4332 |
| sharpe_ratio | -11.5946 |
| sortino_ratio | -5.6878 |
| max_drawdown | 0.9994 |
| cagr | -0.9479 |
| net_avg_win | 15.0611 |
| net_avg_loss | -24.1689 |
| avg_hold_time_bars | 2.6868 |
| exposure | 0.1455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
