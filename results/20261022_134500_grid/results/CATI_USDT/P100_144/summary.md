# EMA Hourly Continuation — CATI/USDT P100_144

**Symbol:** CATI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.4546 |
| net_win_rate | 0.4229 |
| gross_profit_factor | 0.8487 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -6.4332 |
| sortino_ratio | -2.1222 |
| max_drawdown | 0.8952 |
| cagr | -0.6559 |
| net_avg_win | 38.7065 |
| net_avg_loss | -62.3939 |
| avg_hold_time_bars | 4.9075 |
| exposure | 0.1221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
