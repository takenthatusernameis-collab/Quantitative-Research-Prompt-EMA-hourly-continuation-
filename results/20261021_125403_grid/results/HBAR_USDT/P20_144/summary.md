# EMA Hourly Continuation — HBAR/USDT P20_144

**Symbol:** HBAR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.8472 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0528 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -0.9514 |
| sortino_ratio | -0.2584 |
| max_drawdown | 0.3479 |
| cagr | -0.1139 |
| net_avg_win | 78.8984 |
| net_avg_loss | -99.0546 |
| avg_hold_time_bars | 35.2157 |
| exposure | 0.5715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
