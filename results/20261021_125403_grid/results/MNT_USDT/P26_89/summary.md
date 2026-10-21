# EMA Hourly Continuation — MNT/USDT P26_89

**Symbol:** MNT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.6810 |
| net_win_rate | 0.4864 |
| gross_profit_factor | 0.9305 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -2.4055 |
| sortino_ratio | -0.7225 |
| max_drawdown | 0.5829 |
| cagr | -0.2834 |
| net_avg_win | 56.2886 |
| net_avg_loss | -78.2872 |
| avg_hold_time_bars | 15.3688 |
| exposure | 0.3088 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
