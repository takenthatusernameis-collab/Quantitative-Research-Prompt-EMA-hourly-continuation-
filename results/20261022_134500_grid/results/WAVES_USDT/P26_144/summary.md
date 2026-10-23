# EMA Hourly Continuation — WAVES/USDT P26_144

**Symbol:** WAVES/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.5531 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.9248 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -4.9492 |
| sortino_ratio | -1.7532 |
| max_drawdown | 0.8941 |
| cagr | -0.5755 |
| net_avg_win | 37.4581 |
| net_avg_loss | -57.1533 |
| avg_hold_time_bars | 15.3307 |
| exposure | 0.4446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
