# EMA Hourly Continuation — SAFE/USDT P12_89

**Symbol:** SAFE/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.8538 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0396 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -1.0851 |
| sortino_ratio | -0.3411 |
| max_drawdown | 0.4006 |
| cagr | -0.1484 |
| net_avg_win | 78.9673 |
| net_avg_loss | -96.8522 |
| avg_hold_time_bars | 25.2998 |
| exposure | 0.5527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
