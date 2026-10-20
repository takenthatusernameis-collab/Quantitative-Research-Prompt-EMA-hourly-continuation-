# EMA Hourly Continuation — YGG/USDT P8_21

**Symbol:** YGG/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1661 |
| net_profit_factor | 0.4683 |
| net_win_rate | 0.4443 |
| gross_profit_factor | 0.8716 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -10.1792 |
| sortino_ratio | -5.8572 |
| max_drawdown | 0.9993 |
| cagr | -0.9419 |
| net_avg_win | 11.9243 |
| net_avg_loss | -20.3603 |
| avg_hold_time_bars | 3.0933 |
| exposure | 0.2325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
