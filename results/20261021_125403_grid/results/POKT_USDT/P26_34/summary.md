# EMA Hourly Continuation — POKT/USDT P26_34

**Symbol:** POKT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.4494 |
| net_win_rate | 0.3550 |
| gross_profit_factor | 0.6186 |
| gross_win_rate | 0.3550 |
| sharpe_ratio | -4.8841 |
| sortino_ratio | -1.2077 |
| max_drawdown | 0.7648 |
| cagr | -0.4313 |
| net_avg_win | 56.8381 |
| net_avg_loss | -69.6296 |
| avg_hold_time_bars | 6.8730 |
| exposure | 0.0955 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
