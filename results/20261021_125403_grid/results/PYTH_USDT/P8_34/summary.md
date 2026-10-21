# EMA Hourly Continuation — PYTH/USDT P8_34

**Symbol:** PYTH/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.8276 |
| net_win_rate | 0.5007 |
| gross_profit_factor | 1.0384 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -1.9008 |
| sortino_ratio | -0.7262 |
| max_drawdown | 0.6364 |
| cagr | -0.2846 |
| net_avg_win | 76.6832 |
| net_avg_loss | -92.9193 |
| avg_hold_time_bars | 8.4613 |
| exposure | 0.2735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
