# EMA Hourly Continuation — AEVO/USDT P50_144

**Symbol:** AEVO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.7105 |
| net_win_rate | 0.5020 |
| gross_profit_factor | 1.0056 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -2.3259 |
| sortino_ratio | -0.7372 |
| max_drawdown | 0.5900 |
| cagr | -0.2930 |
| net_avg_win | 56.7887 |
| net_avg_loss | -80.5639 |
| avg_hold_time_bars | 14.1195 |
| exposure | 0.3207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
