# EMA Hourly Continuation — BAT/USDT P100_144

**Symbol:** BAT/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.4025 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.8865 |
| gross_win_rate | 0.4676 |
| sharpe_ratio | -5.6901 |
| sortino_ratio | -1.7597 |
| max_drawdown | 0.8903 |
| cagr | -0.5836 |
| net_avg_win | 28.5277 |
| net_avg_loss | -55.3281 |
| avg_hold_time_bars | 4.3069 |
| exposure | 0.0938 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
