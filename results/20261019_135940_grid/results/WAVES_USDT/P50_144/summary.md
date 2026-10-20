# EMA Hourly Continuation — WAVES/USDT P50_144

**Symbol:** WAVES/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.4657 |
| net_win_rate | 0.4305 |
| gross_profit_factor | 0.8177 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -5.7784 |
| sortino_ratio | -1.9829 |
| max_drawdown | 0.9203 |
| cagr | -0.6247 |
| net_avg_win | 31.0204 |
| net_avg_loss | -50.3494 |
| avg_hold_time_bars | 10.2764 |
| exposure | 0.2789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
