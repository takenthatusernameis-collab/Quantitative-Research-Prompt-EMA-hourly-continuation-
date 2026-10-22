# EMA Hourly Continuation — ALEX/USDT P8_50

**Symbol:** ALEX/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 851 |
| net_profit_factor | 0.6171 |
| net_win_rate | 0.4477 |
| gross_profit_factor | 1.0084 |
| gross_win_rate | 0.4653 |
| sharpe_ratio | -5.6873 |
| sortino_ratio | -2.2999 |
| max_drawdown | 0.9496 |
| cagr | -0.6851 |
| net_avg_win | 39.9790 |
| net_avg_loss | -52.5162 |
| avg_hold_time_bars | 13.4524 |
| exposure | 0.5204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
