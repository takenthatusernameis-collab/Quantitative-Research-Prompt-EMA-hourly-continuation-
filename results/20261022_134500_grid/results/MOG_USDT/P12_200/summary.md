# EMA Hourly Continuation — MOG/USDT P12_200

**Symbol:** MOG/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.6855 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.8969 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -2.5728 |
| sortino_ratio | -0.7264 |
| max_drawdown | 0.5659 |
| cagr | -0.2932 |
| net_avg_win | 69.5952 |
| net_avg_loss | -87.7539 |
| avg_hold_time_bars | 39.5094 |
| exposure | 0.7287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
