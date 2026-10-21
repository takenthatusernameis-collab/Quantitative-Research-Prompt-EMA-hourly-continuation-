# EMA Hourly Continuation — PYTH/USDT P12_144

**Symbol:** PYTH/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.8965 |
| net_win_rate | 0.5119 |
| gross_profit_factor | 1.0417 |
| gross_win_rate | 0.5119 |
| sharpe_ratio | -0.6548 |
| sortino_ratio | -0.1823 |
| max_drawdown | 0.3552 |
| cagr | -0.0840 |
| net_avg_win | 88.8273 |
| net_avg_loss | -103.9252 |
| avg_hold_time_bars | 39.2149 |
| exposure | 0.6720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
