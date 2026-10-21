# EMA Hourly Continuation — 1INCH/USDT P20_26

**Symbol:** 1INCH/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.5698 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.8939 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -2.5654 |
| sortino_ratio | -0.5485 |
| max_drawdown | 0.4704 |
| cagr | -0.2223 |
| net_avg_win | 59.0331 |
| net_avg_loss | -93.7855 |
| avg_hold_time_bars | 4.3846 |
| exposure | 0.0440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
