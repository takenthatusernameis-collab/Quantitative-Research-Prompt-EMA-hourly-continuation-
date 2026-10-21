# EMA Hourly Continuation — GMX/USDT P21_34

**Symbol:** GMX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.5889 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8823 |
| gross_win_rate | 0.4596 |
| sharpe_ratio | -3.8276 |
| sortino_ratio | -1.1885 |
| max_drawdown | 0.7466 |
| cagr | -0.4191 |
| net_avg_win | 49.3665 |
| net_avg_loss | -71.2870 |
| avg_hold_time_bars | 5.8511 |
| exposure | 0.1250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
