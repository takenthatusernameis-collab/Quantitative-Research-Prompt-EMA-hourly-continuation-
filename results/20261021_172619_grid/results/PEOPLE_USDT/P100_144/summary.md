# EMA Hourly Continuation — PEOPLE/USDT P100_144

**Symbol:** PEOPLE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.7915 |
| net_win_rate | 0.5149 |
| gross_profit_factor | 1.0592 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -1.1890 |
| sortino_ratio | -0.2794 |
| max_drawdown | 0.3559 |
| cagr | -0.1205 |
| net_avg_win | 76.1417 |
| net_avg_loss | -102.1179 |
| avg_hold_time_bars | 7.3619 |
| exposure | 0.0893 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
