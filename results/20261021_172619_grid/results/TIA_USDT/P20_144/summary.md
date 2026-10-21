# EMA Hourly Continuation — TIA/USDT P20_144

**Symbol:** TIA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.8833 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0118 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -0.6772 |
| sortino_ratio | -0.1755 |
| max_drawdown | 0.2461 |
| cagr | -0.0806 |
| net_avg_win | 87.2775 |
| net_avg_loss | -100.6366 |
| avg_hold_time_bars | 37.7798 |
| exposure | 0.5615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
