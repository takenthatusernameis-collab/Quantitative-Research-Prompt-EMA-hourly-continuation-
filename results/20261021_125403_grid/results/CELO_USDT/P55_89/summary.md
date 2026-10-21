# EMA Hourly Continuation — CELO/USDT P55_89

**Symbol:** CELO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.9102 |
| net_win_rate | 0.5556 |
| gross_profit_factor | 1.2469 |
| gross_win_rate | 0.5556 |
| sharpe_ratio | -0.4644 |
| sortino_ratio | -0.1195 |
| max_drawdown | 0.1617 |
| cagr | -0.0564 |
| net_avg_win | 78.9283 |
| net_avg_loss | -108.3920 |
| avg_hold_time_bars | 7.8190 |
| exposure | 0.1115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
