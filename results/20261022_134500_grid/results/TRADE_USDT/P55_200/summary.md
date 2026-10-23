# EMA Hourly Continuation — TRADE/USDT P55_200

**Symbol:** TRADE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.5299 |
| net_win_rate | 0.3988 |
| gross_profit_factor | 0.6920 |
| gross_win_rate | 0.4018 |
| sharpe_ratio | -3.7948 |
| sortino_ratio | -0.9682 |
| max_drawdown | 0.6967 |
| cagr | -0.3684 |
| net_avg_win | 58.4512 |
| net_avg_loss | -73.1714 |
| avg_hold_time_bars | 21.6888 |
| exposure | 0.3263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
