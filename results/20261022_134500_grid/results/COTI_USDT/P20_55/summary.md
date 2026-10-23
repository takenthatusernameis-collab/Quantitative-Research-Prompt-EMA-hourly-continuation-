# EMA Hourly Continuation — COTI/USDT P20_55

**Symbol:** COTI/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1010 |
| net_profit_factor | 0.6117 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.9687 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -5.9027 |
| sortino_ratio | -2.6505 |
| max_drawdown | 0.9613 |
| cagr | -0.7192 |
| net_avg_win | 31.8632 |
| net_avg_loss | -46.0660 |
| avg_hold_time_bars | 5.1000 |
| exposure | 0.2341 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
