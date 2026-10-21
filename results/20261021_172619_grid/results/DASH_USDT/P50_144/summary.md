# EMA Hourly Continuation — DASH/USDT P50_144

**Symbol:** DASH/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7817 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 1.0159 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -1.3732 |
| sortino_ratio | -0.3685 |
| max_drawdown | 0.4193 |
| cagr | -0.1565 |
| net_avg_win | 70.3792 |
| net_avg_loss | -92.1138 |
| avg_hold_time_bars | 13.5829 |
| exposure | 0.2161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
