# EMA Hourly Continuation — KCS/USDT P12_144

**Symbol:** KCS/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.5906 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.9159 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -3.6282 |
| sortino_ratio | -1.0491 |
| max_drawdown | 0.7128 |
| cagr | -0.3823 |
| net_avg_win | 53.8588 |
| net_avg_loss | -77.5714 |
| avg_hold_time_bars | 33.0587 |
| exposure | 0.6146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
