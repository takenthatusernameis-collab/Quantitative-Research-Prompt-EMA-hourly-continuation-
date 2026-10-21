# EMA Hourly Continuation — DEXE/USDT P50_144

**Symbol:** DEXE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.8699 |
| net_win_rate | 0.5227 |
| gross_profit_factor | 1.0644 |
| gross_win_rate | 0.5227 |
| sharpe_ratio | -0.5855 |
| sortino_ratio | -0.1367 |
| max_drawdown | 0.2898 |
| cagr | -0.0633 |
| net_avg_win | 73.3428 |
| net_avg_loss | -92.3429 |
| avg_hold_time_bars | 37.0682 |
| exposure | 0.4448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
