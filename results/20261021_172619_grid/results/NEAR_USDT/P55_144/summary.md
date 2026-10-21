# EMA Hourly Continuation — NEAR/USDT P55_144

**Symbol:** NEAR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.8442 |
| net_win_rate | 0.5124 |
| gross_profit_factor | 1.0345 |
| gross_win_rate | 0.5124 |
| sharpe_ratio | -0.8733 |
| sortino_ratio | -0.2251 |
| max_drawdown | 0.2749 |
| cagr | -0.1001 |
| net_avg_win | 76.4217 |
| net_avg_loss | -95.1393 |
| avg_hold_time_bars | 13.1646 |
| exposure | 0.1927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
