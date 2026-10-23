# EMA Hourly Continuation — TRADE/USDT P21_50

**Symbol:** TRADE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 780 |
| net_profit_factor | 0.5162 |
| net_win_rate | 0.4308 |
| gross_profit_factor | 0.8472 |
| gross_win_rate | 0.4385 |
| sharpe_ratio | -6.5312 |
| sortino_ratio | -2.5434 |
| max_drawdown | 0.9615 |
| cagr | -0.7216 |
| net_avg_win | 30.4790 |
| net_avg_loss | -44.6798 |
| avg_hold_time_bars | 6.0936 |
| exposure | 0.2160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
