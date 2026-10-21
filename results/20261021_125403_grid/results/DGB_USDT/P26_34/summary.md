# EMA Hourly Continuation — DGB/USDT P26_34

**Symbol:** DGB/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 169 |
| net_profit_factor | 0.6358 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8949 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -1.9775 |
| sortino_ratio | -0.3674 |
| max_drawdown | 0.4219 |
| cagr | -0.1555 |
| net_avg_win | 77.4342 |
| net_avg_loss | -104.3876 |
| avg_hold_time_bars | 6.5858 |
| exposure | 0.0506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
