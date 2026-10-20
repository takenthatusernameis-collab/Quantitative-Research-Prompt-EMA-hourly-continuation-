# EMA Hourly Continuation — SLP/USDT P34_50

**Symbol:** SLP/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1061 |
| net_profit_factor | 0.4273 |
| net_win_rate | 0.3930 |
| gross_profit_factor | 0.8916 |
| gross_win_rate | 0.4194 |
| sharpe_ratio | -11.0249 |
| sortino_ratio | -5.1468 |
| max_drawdown | 0.9985 |
| cagr | -0.9247 |
| net_avg_win | 17.8662 |
| net_avg_loss | -27.0731 |
| avg_hold_time_bars | 2.5052 |
| exposure | 0.1208 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
