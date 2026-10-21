# EMA Hourly Continuation — RENDER/USDT P12_144

**Symbol:** RENDER/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.9018 |
| net_win_rate | 0.5157 |
| gross_profit_factor | 1.0478 |
| gross_win_rate | 0.5157 |
| sharpe_ratio | -0.5717 |
| sortino_ratio | -0.1576 |
| max_drawdown | 0.2525 |
| cagr | -0.0740 |
| net_avg_win | 85.7941 |
| net_avg_loss | -101.3177 |
| avg_hold_time_bars | 41.1289 |
| exposure | 0.6903 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
