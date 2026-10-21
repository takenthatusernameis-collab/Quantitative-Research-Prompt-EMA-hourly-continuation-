# EMA Hourly Continuation — PYTH/USDT P50_144

**Symbol:** PYTH/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.8399 |
| net_win_rate | 0.5072 |
| gross_profit_factor | 1.0162 |
| gross_win_rate | 0.5072 |
| sharpe_ratio | -0.9605 |
| sortino_ratio | -0.2567 |
| max_drawdown | 0.3074 |
| cagr | -0.1133 |
| net_avg_win | 77.6897 |
| net_avg_loss | -95.2031 |
| avg_hold_time_bars | 16.7550 |
| exposure | 0.2643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
