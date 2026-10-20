# EMA Hourly Continuation — DEXE/USDT P50_144

**Symbol:** DEXE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6682 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 0.9734 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -1.9453 |
| sortino_ratio | -0.5156 |
| max_drawdown | 0.5425 |
| cagr | -0.2173 |
| net_avg_win | 51.9936 |
| net_avg_loss | -79.5965 |
| avg_hold_time_bars | 28.4659 |
| exposure | 0.4555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
