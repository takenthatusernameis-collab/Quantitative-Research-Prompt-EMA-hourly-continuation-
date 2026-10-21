# EMA Hourly Continuation — BRETT/USDT P20_100

**Symbol:** BRETT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.8026 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9274 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -1.4451 |
| sortino_ratio | -0.4338 |
| max_drawdown | 0.3867 |
| cagr | -0.1829 |
| net_avg_win | 76.6392 |
| net_avg_loss | -88.8877 |
| avg_hold_time_bars | 20.1289 |
| exposure | 0.4058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
