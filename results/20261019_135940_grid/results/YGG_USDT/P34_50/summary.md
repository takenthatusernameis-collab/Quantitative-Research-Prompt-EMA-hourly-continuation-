# EMA Hourly Continuation — YGG/USDT P34_50

**Symbol:** YGG/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 941 |
| net_profit_factor | 0.5172 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 1.0019 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -7.5315 |
| sortino_ratio | -3.2521 |
| max_drawdown | 0.9829 |
| cagr | -0.7995 |
| net_avg_win | 24.7120 |
| net_avg_loss | -39.5218 |
| avg_hold_time_bars | 2.8948 |
| exposure | 0.1233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
