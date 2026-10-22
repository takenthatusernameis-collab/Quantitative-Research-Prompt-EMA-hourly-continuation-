# EMA Hourly Continuation — RAY/USDT P50_144

**Symbol:** RAY/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.6072 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.8758 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -3.2958 |
| sortino_ratio | -1.0376 |
| max_drawdown | 0.7322 |
| cagr | -0.3890 |
| net_avg_win | 46.7025 |
| net_avg_loss | -68.7205 |
| avg_hold_time_bars | 11.4679 |
| exposure | 0.2596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
