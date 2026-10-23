# EMA Hourly Continuation — TRADE/USDT P12_26

**Symbol:** TRADE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1155 |
| net_profit_factor | 0.4475 |
| net_win_rate | 0.3991 |
| gross_profit_factor | 0.8705 |
| gross_win_rate | 0.4121 |
| sharpe_ratio | -10.5873 |
| sortino_ratio | -5.0716 |
| max_drawdown | 0.9987 |
| cagr | -0.9255 |
| net_avg_win | 17.5448 |
| net_avg_loss | -26.0425 |
| avg_hold_time_bars | 3.9965 |
| exposure | 0.2098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
