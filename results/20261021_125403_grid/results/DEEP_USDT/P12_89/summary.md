# EMA Hourly Continuation — DEEP/USDT P12_89

**Symbol:** DEEP/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.9557 |
| net_win_rate | 0.5289 |
| gross_profit_factor | 1.1150 |
| gross_win_rate | 0.5289 |
| sharpe_ratio | -0.2849 |
| sortino_ratio | -0.0893 |
| max_drawdown | 0.3436 |
| cagr | -0.0474 |
| net_avg_win | 100.0929 |
| net_avg_loss | -117.6048 |
| avg_hold_time_bars | 24.9763 |
| exposure | 0.5374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
