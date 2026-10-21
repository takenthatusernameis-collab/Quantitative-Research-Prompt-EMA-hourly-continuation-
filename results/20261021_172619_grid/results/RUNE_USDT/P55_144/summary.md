# EMA Hourly Continuation — RUNE/USDT P55_144

**Symbol:** RUNE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.8916 |
| net_win_rate | 0.5375 |
| gross_profit_factor | 1.1367 |
| gross_win_rate | 0.5375 |
| sharpe_ratio | -0.5015 |
| sortino_ratio | -0.1272 |
| max_drawdown | 0.3048 |
| cagr | -0.0595 |
| net_avg_win | 71.1613 |
| net_avg_loss | -92.7416 |
| avg_hold_time_bars | 18.8176 |
| exposure | 0.2626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
