# EMA Hourly Continuation — SOL/USDT P34_89

**Symbol:** SOL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.5029 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.9281 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -6.0712 |
| sortino_ratio | -2.2087 |
| max_drawdown | 0.9420 |
| cagr | -0.6690 |
| net_avg_win | 30.8052 |
| net_avg_loss | -51.8285 |
| avg_hold_time_bars | 6.9777 |
| exposure | 0.2131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
