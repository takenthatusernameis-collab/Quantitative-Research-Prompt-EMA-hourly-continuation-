# EMA Hourly Continuation — TFUEL/USDT P26_144

**Symbol:** TFUEL/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.5958 |
| net_win_rate | 0.4224 |
| gross_profit_factor | 0.7606 |
| gross_win_rate | 0.4224 |
| sharpe_ratio | -3.9803 |
| sortino_ratio | -1.2667 |
| max_drawdown | 0.7772 |
| cagr | -0.4421 |
| net_avg_win | 52.8350 |
| net_avg_loss | -64.8481 |
| avg_hold_time_bars | 16.9862 |
| exposure | 0.3912 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
