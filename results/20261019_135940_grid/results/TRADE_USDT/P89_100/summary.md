# EMA Hourly Continuation — TRADE/USDT P89_100

**Symbol:** TRADE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.1927 |
| net_win_rate | 0.3019 |
| gross_profit_factor | 0.4390 |
| gross_win_rate | 0.3212 |
| sharpe_ratio | -9.6124 |
| sortino_ratio | -3.0408 |
| max_drawdown | 0.9838 |
| cagr | -0.8045 |
| net_avg_win | 16.6531 |
| net_avg_loss | -37.3684 |
| avg_hold_time_bars | 2.7623 |
| exposure | 0.0586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
