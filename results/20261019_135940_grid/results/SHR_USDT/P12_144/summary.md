# EMA Hourly Continuation — SHR/USDT P12_144

**Symbol:** SHR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 931 |
| net_profit_factor | 0.3959 |
| net_win_rate | 0.3298 |
| gross_profit_factor | 0.5441 |
| gross_win_rate | 0.3308 |
| sharpe_ratio | -9.0363 |
| sortino_ratio | -3.8203 |
| max_drawdown | 0.9908 |
| cagr | -0.8430 |
| net_avg_win | 21.1471 |
| net_avg_loss | -26.2797 |
| avg_hold_time_bars | 12.7025 |
| exposure | 0.5351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
