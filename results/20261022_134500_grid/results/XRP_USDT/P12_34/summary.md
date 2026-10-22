# EMA Hourly Continuation — XRP/USDT P12_34

**Symbol:** XRP/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1317 |
| net_profit_factor | 0.2870 |
| net_win_rate | 0.4085 |
| gross_profit_factor | 0.8990 |
| gross_win_rate | 0.4594 |
| sharpe_ratio | -12.4367 |
| sortino_ratio | -6.3994 |
| max_drawdown | 0.9998 |
| cagr | -0.9657 |
| net_avg_win | 7.4808 |
| net_avg_loss | -18.0007 |
| avg_hold_time_bars | 3.6302 |
| exposure | 0.2173 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
