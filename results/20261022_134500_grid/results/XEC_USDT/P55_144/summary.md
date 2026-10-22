# EMA Hourly Continuation — XEC/USDT P55_144

**Symbol:** XEC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.4519 |
| net_win_rate | 0.4231 |
| gross_profit_factor | 0.7745 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -5.2675 |
| sortino_ratio | -1.6930 |
| max_drawdown | 0.8765 |
| cagr | -0.5559 |
| net_avg_win | 32.6385 |
| net_avg_loss | -52.9657 |
| avg_hold_time_bars | 11.0327 |
| exposure | 0.2596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
