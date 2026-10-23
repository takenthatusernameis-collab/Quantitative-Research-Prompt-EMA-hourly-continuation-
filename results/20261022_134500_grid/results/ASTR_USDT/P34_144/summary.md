# EMA Hourly Continuation — ASTR/USDT P34_144

**Symbol:** ASTR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.6980 |
| net_win_rate | 0.5066 |
| gross_profit_factor | 1.0641 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -2.3416 |
| sortino_ratio | -0.7067 |
| max_drawdown | 0.6117 |
| cagr | -0.2825 |
| net_avg_win | 56.7501 |
| net_avg_loss | -83.4707 |
| avg_hold_time_bars | 19.6206 |
| exposure | 0.4049 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
