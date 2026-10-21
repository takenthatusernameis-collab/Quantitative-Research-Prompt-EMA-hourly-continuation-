# EMA Hourly Continuation — EWT/USDT P12_144

**Symbol:** EWT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6941 |
| net_win_rate | 0.4579 |
| gross_profit_factor | 0.8304 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -2.2767 |
| sortino_ratio | -0.6763 |
| max_drawdown | 0.6110 |
| cagr | -0.2676 |
| net_avg_win | 61.2401 |
| net_avg_loss | -74.5128 |
| avg_hold_time_bars | 25.9248 |
| exposure | 0.5173 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
