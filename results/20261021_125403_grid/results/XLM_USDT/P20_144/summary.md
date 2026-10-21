# EMA Hourly Continuation — XLM/USDT P20_144

**Symbol:** XLM/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7494 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9579 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -1.5799 |
| sortino_ratio | -0.4224 |
| max_drawdown | 0.4143 |
| cagr | -0.1771 |
| net_avg_win | 67.2750 |
| net_avg_loss | -86.7489 |
| avg_hold_time_bars | 35.1057 |
| exposure | 0.5585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
