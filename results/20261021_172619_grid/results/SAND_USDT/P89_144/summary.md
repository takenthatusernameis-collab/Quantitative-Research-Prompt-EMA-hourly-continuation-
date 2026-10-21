# EMA Hourly Continuation — SAND/USDT P89_144

**Symbol:** SAND/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.6025 |
| net_win_rate | 0.4480 |
| gross_profit_factor | 0.8169 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -2.5277 |
| sortino_ratio | -0.5693 |
| max_drawdown | 0.4931 |
| cagr | -0.2303 |
| net_avg_win | 65.1831 |
| net_avg_loss | -87.8092 |
| avg_hold_time_bars | 7.2760 |
| exposure | 0.0827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
