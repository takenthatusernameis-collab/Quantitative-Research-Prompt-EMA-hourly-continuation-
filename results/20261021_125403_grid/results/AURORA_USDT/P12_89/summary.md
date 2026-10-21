# EMA Hourly Continuation — AURORA/USDT P12_89

**Symbol:** AURORA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.7151 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.9151 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -2.3982 |
| sortino_ratio | -0.7388 |
| max_drawdown | 0.5820 |
| cagr | -0.2885 |
| net_avg_win | 64.9593 |
| net_avg_loss | -81.9786 |
| avg_hold_time_bars | 23.8825 |
| exposure | 0.5080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
