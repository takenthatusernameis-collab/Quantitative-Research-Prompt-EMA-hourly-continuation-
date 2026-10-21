# EMA Hourly Continuation — POKT/USDT P12_144

**Symbol:** POKT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.6454 |
| net_win_rate | 0.4248 |
| gross_profit_factor | 0.7882 |
| gross_win_rate | 0.4248 |
| sharpe_ratio | -3.2946 |
| sortino_ratio | -0.9844 |
| max_drawdown | 0.6877 |
| cagr | -0.3657 |
| net_avg_win | 64.7340 |
| net_avg_loss | -74.0654 |
| avg_hold_time_bars | 31.6394 |
| exposure | 0.6472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
