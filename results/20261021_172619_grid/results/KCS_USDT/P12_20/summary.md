# EMA Hourly Continuation — KCS/USDT P12_20

**Symbol:** KCS/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.3406 |
| net_win_rate | 0.4048 |
| gross_profit_factor | 0.7248 |
| gross_win_rate | 0.4152 |
| sharpe_ratio | -5.4137 |
| sortino_ratio | -1.3449 |
| max_drawdown | 0.8039 |
| cagr | -0.4710 |
| net_avg_win | 35.2203 |
| net_avg_loss | -70.3505 |
| avg_hold_time_bars | 7.0069 |
| exposure | 0.0920 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
