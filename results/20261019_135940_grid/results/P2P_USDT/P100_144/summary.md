# EMA Hourly Continuation — P2P/USDT P100_144

**Symbol:** P2P/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.4514 |
| net_win_rate | 0.4050 |
| gross_profit_factor | 0.6731 |
| gross_win_rate | 0.4050 |
| sharpe_ratio | -4.8914 |
| sortino_ratio | -1.4283 |
| max_drawdown | 0.8295 |
| cagr | -0.5045 |
| net_avg_win | 38.5195 |
| net_avg_loss | -58.0900 |
| avg_hold_time_bars | 5.6590 |
| exposure | 0.1124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
