# EMA Hourly Continuation — KMNO/USDT P20_144

**Symbol:** KMNO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.8851 |
| net_win_rate | 0.5159 |
| gross_profit_factor | 1.0672 |
| gross_win_rate | 0.5159 |
| sharpe_ratio | -0.7185 |
| sortino_ratio | -0.1929 |
| max_drawdown | 0.2599 |
| cagr | -0.0883 |
| net_avg_win | 88.4011 |
| net_avg_loss | -106.4551 |
| avg_hold_time_bars | 32.9333 |
| exposure | 0.5246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
