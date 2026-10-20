# EMA Hourly Continuation — TFUEL/USDT P20_144

**Symbol:** TFUEL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 718 |
| net_profit_factor | 0.5424 |
| net_win_rate | 0.4178 |
| gross_profit_factor | 0.8215 |
| gross_win_rate | 0.4262 |
| sharpe_ratio | -6.1978 |
| sortino_ratio | -2.3184 |
| max_drawdown | 0.9426 |
| cagr | -0.6765 |
| net_avg_win | 37.2246 |
| net_avg_loss | -49.2516 |
| avg_hold_time_bars | 14.5070 |
| exposure | 0.4713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
