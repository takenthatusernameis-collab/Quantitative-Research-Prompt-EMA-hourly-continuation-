# EMA Hourly Continuation — TNSR/USDT P21_89

**Symbol:** TNSR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.8477 |
| net_win_rate | 0.5124 |
| gross_profit_factor | 1.0457 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -1.2180 |
| sortino_ratio | -0.3997 |
| max_drawdown | 0.4349 |
| cagr | -0.1703 |
| net_avg_win | 77.6778 |
| net_avg_loss | -96.2922 |
| avg_hold_time_bars | 15.2838 |
| exposure | 0.3631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
