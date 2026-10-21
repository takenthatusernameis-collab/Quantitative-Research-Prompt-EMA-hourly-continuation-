# EMA Hourly Continuation — CGPT/USDT P12_144

**Symbol:** CGPT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.9009 |
| net_win_rate | 0.5145 |
| gross_profit_factor | 1.0577 |
| gross_win_rate | 0.5145 |
| sharpe_ratio | -0.6053 |
| sortino_ratio | -0.1618 |
| max_drawdown | 0.2892 |
| cagr | -0.0751 |
| net_avg_win | 90.9205 |
| net_avg_loss | -106.9249 |
| avg_hold_time_bars | 43.5318 |
| exposure | 0.6846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
