# EMA Hourly Continuation — KCS/USDT P100_200

**Symbol:** KCS/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.2638 |
| net_win_rate | 0.3995 |
| gross_profit_factor | 0.7266 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -6.8376 |
| sortino_ratio | -1.9967 |
| max_drawdown | 0.9215 |
| cagr | -0.6346 |
| net_avg_win | 19.9835 |
| net_avg_loss | -50.4010 |
| avg_hold_time_bars | 9.9274 |
| exposure | 0.1864 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
