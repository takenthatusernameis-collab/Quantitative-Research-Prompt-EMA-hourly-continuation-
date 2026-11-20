# EMA Hourly Continuation — P2P/USDT P89_200

**Symbol:** P2P/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.5999 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.7815 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -2.7349 |
| sortino_ratio | -0.7098 |
| max_drawdown | 0.5944 |
| cagr | -0.2878 |
| net_avg_win | 56.5870 |
| net_avg_loss | -75.4602 |
| avg_hold_time_bars | 13.2807 |
| exposure | 0.2065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
