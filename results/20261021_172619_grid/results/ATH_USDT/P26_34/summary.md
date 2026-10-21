# EMA Hourly Continuation — ATH/USDT P26_34

**Symbol:** ATH/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 146 |
| net_profit_factor | 0.9703 |
| net_win_rate | 0.5685 |
| gross_profit_factor | 1.3050 |
| gross_win_rate | 0.5685 |
| sharpe_ratio | -0.0794 |
| sortino_ratio | -0.0145 |
| max_drawdown | 0.1199 |
| cagr | -0.0093 |
| net_avg_win | 85.2832 |
| net_avg_loss | -115.7936 |
| avg_hold_time_bars | 4.4932 |
| exposure | 0.0318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
