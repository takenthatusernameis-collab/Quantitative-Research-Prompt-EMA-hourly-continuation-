# EMA Hourly Continuation — CHR/USDT P12_200

**Symbol:** CHR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.7006 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9261 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -1.9591 |
| sortino_ratio | -0.5080 |
| max_drawdown | 0.4909 |
| cagr | -0.2124 |
| net_avg_win | 65.3689 |
| net_avg_loss | -85.8793 |
| avg_hold_time_bars | 50.7012 |
| exposure | 0.7755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
