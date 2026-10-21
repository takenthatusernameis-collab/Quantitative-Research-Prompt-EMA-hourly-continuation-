# EMA Hourly Continuation — MANA/USDT P12_89

**Symbol:** MANA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.7588 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9549 |
| gross_win_rate | 0.4806 |
| sharpe_ratio | -2.0580 |
| sortino_ratio | -0.6146 |
| max_drawdown | 0.5359 |
| cagr | -0.2469 |
| net_avg_win | 75.9402 |
| net_avg_loss | -92.6161 |
| avg_hold_time_bars | 28.0843 |
| exposure | 0.5604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
