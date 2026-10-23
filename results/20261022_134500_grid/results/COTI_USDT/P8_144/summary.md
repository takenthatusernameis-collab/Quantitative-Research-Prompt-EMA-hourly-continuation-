# EMA Hourly Continuation — COTI/USDT P8_144

**Symbol:** COTI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.7263 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 1.0117 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -2.4991 |
| sortino_ratio | -0.8474 |
| max_drawdown | 0.6705 |
| cagr | -0.3368 |
| net_avg_win | 58.6755 |
| net_avg_loss | -79.1547 |
| avg_hold_time_bars | 26.8452 |
| exposure | 0.7175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
