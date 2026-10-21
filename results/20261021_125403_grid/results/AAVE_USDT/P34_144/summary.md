# EMA Hourly Continuation — AAVE/USDT P34_144

**Symbol:** AAVE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.9584 |
| net_win_rate | 0.5434 |
| gross_profit_factor | 1.1768 |
| gross_win_rate | 0.5434 |
| sharpe_ratio | -0.1961 |
| sortino_ratio | -0.0528 |
| max_drawdown | 0.1952 |
| cagr | -0.0293 |
| net_avg_win | 88.0824 |
| net_avg_loss | -109.3611 |
| avg_hold_time_bars | 22.4017 |
| exposure | 0.3523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
