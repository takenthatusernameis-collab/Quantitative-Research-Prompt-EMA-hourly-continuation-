# EMA Hourly Continuation — MANTA/USDT P26_55

**Symbol:** MANTA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 929 |
| net_profit_factor | 0.5028 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 0.8434 |
| gross_win_rate | 0.4446 |
| sharpe_ratio | -7.3263 |
| sortino_ratio | -3.1530 |
| max_drawdown | 0.9792 |
| cagr | -0.7849 |
| net_avg_win | 24.5682 |
| net_avg_loss | -37.4338 |
| avg_hold_time_bars | 4.4306 |
| exposure | 0.1871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
