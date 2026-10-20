# EMA Hourly Continuation — POKT/USDT P8_144

**Symbol:** POKT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 784 |
| net_profit_factor | 0.5721 |
| net_win_rate | 0.4184 |
| gross_profit_factor | 0.8519 |
| gross_win_rate | 0.4260 |
| sharpe_ratio | -5.8880 |
| sortino_ratio | -2.2984 |
| max_drawdown | 0.9411 |
| cagr | -0.6704 |
| net_avg_win | 38.2769 |
| net_avg_loss | -48.1287 |
| avg_hold_time_bars | 19.2117 |
| exposure | 0.6816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
