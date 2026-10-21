# EMA Hourly Continuation — AERO/USDT P89_144

**Symbol:** AERO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.7510 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9476 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -1.2946 |
| sortino_ratio | -0.2752 |
| max_drawdown | 0.2721 |
| cagr | -0.1188 |
| net_avg_win | 75.9741 |
| net_avg_loss | -96.6887 |
| avg_hold_time_bars | 8.1131 |
| exposure | 0.0815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
