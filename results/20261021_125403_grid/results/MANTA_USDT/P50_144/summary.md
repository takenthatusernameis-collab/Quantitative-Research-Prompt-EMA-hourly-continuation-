# EMA Hourly Continuation — MANTA/USDT P50_144

**Symbol:** MANTA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.7435 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9042 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -1.6463 |
| sortino_ratio | -0.4242 |
| max_drawdown | 0.3883 |
| cagr | -0.1778 |
| net_avg_win | 72.1569 |
| net_avg_loss | -88.5351 |
| avg_hold_time_bars | 22.7064 |
| exposure | 0.3375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
