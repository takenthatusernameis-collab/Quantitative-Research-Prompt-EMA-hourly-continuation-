# EMA Hourly Continuation — SAFE/USDT P12_50

**Symbol:** SAFE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1010 |
| net_profit_factor | 0.5483 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.8792 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -5.2744 |
| sortino_ratio | -2.3688 |
| max_drawdown | 0.9416 |
| cagr | -0.6775 |
| net_avg_win | 23.7286 |
| net_avg_loss | -39.3531 |
| avg_hold_time_bars | 8.2822 |
| exposure | 0.3831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
