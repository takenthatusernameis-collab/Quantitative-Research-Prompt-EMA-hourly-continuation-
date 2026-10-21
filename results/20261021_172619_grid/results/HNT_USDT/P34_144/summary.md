# EMA Hourly Continuation — HNT/USDT P34_144

**Symbol:** HNT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.6939 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.8250 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -1.8467 |
| sortino_ratio | -0.4982 |
| max_drawdown | 0.5349 |
| cagr | -0.2054 |
| net_avg_win | 58.8237 |
| net_avg_loss | -74.6185 |
| avg_hold_time_bars | 23.2382 |
| exposure | 0.3813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
