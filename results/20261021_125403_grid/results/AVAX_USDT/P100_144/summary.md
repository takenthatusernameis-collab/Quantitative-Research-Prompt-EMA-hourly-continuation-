# EMA Hourly Continuation — AVAX/USDT P100_144

**Symbol:** AVAX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 200 |
| net_profit_factor | 0.6831 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9458 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -1.6308 |
| sortino_ratio | -0.3307 |
| max_drawdown | 0.3332 |
| cagr | -0.1407 |
| net_avg_win | 69.6687 |
| net_avg_loss | -97.9863 |
| avg_hold_time_bars | 6.1500 |
| exposure | 0.0559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
