# EMA Hourly Continuation — ROSE/USDT P12_100

**Symbol:** ROSE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.8692 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0368 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -0.9565 |
| sortino_ratio | -0.2821 |
| max_drawdown | 0.3905 |
| cagr | -0.1247 |
| net_avg_win | 87.4900 |
| net_avg_loss | -104.5257 |
| avg_hold_time_bars | 32.1840 |
| exposure | 0.6203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
