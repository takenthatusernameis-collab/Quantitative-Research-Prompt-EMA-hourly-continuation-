# EMA Hourly Continuation — STRK/USDT P20_144

**Symbol:** STRK/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.8842 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0417 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -0.7435 |
| sortino_ratio | -0.2115 |
| max_drawdown | 0.2972 |
| cagr | -0.0962 |
| net_avg_win | 85.2437 |
| net_avg_loss | -100.9213 |
| avg_hold_time_bars | 28.2417 |
| exposure | 0.5045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
