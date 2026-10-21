# EMA Hourly Continuation — TRX/USDT P12_89

**Symbol:** TRX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.5419 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9401 |
| gross_win_rate | 0.4918 |
| sharpe_ratio | -4.3891 |
| sortino_ratio | -1.3962 |
| max_drawdown | 0.8115 |
| cagr | -0.4759 |
| net_avg_win | 39.8977 |
| net_avg_loss | -70.0877 |
| avg_hold_time_bars | 21.1680 |
| exposure | 0.4695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
