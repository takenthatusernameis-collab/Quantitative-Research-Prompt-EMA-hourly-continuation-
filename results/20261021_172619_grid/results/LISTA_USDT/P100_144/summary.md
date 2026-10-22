# EMA Hourly Continuation — LISTA/USDT P100_144

**Symbol:** LISTA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.7035 |
| net_win_rate | 0.4834 |
| gross_profit_factor | 0.9303 |
| gross_win_rate | 0.4834 |
| sharpe_ratio | -1.8816 |
| sortino_ratio | -0.4593 |
| max_drawdown | 0.4045 |
| cagr | -0.1903 |
| net_avg_win | 70.4824 |
| net_avg_loss | -93.7432 |
| avg_hold_time_bars | 7.0221 |
| exposure | 0.0931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
