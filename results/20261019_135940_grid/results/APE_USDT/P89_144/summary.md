# EMA Hourly Continuation — APE/USDT P89_144

**Symbol:** APE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.5215 |
| net_win_rate | 0.4884 |
| gross_profit_factor | 0.9413 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -4.1724 |
| sortino_ratio | -1.3398 |
| max_drawdown | 0.8044 |
| cagr | -0.4778 |
| net_avg_win | 34.6556 |
| net_avg_loss | -63.4405 |
| avg_hold_time_bars | 4.9228 |
| exposure | 0.1159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
