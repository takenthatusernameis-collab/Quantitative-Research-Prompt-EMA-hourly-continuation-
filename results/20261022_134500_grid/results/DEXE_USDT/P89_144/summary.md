# EMA Hourly Continuation — DEXE/USDT P89_144

**Symbol:** DEXE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.4964 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.8542 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -3.6141 |
| sortino_ratio | -1.0066 |
| max_drawdown | 0.7156 |
| cagr | -0.3862 |
| net_avg_win | 37.6444 |
| net_avg_loss | -68.7686 |
| avg_hold_time_bars | 11.9589 |
| exposure | 0.2115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
