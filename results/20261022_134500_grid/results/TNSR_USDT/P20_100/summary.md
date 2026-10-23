# EMA Hourly Continuation — TNSR/USDT P20_100

**Symbol:** TNSR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.7195 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 1.0014 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -2.9817 |
| sortino_ratio | -1.0725 |
| max_drawdown | 0.7498 |
| cagr | -0.3994 |
| net_avg_win | 57.6555 |
| net_avg_loss | -77.2498 |
| avg_hold_time_bars | 14.5686 |
| exposure | 0.4325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
