# EMA Hourly Continuation — CELO/USDT P50_89

**Symbol:** CELO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 613 |
| net_profit_factor | 0.6198 |
| net_win_rate | 0.5237 |
| gross_profit_factor | 1.0925 |
| gross_win_rate | 0.5334 |
| sharpe_ratio | -3.4020 |
| sortino_ratio | -1.1925 |
| max_drawdown | 0.7693 |
| cagr | -0.4336 |
| net_avg_win | 38.6825 |
| net_avg_loss | -68.6062 |
| avg_hold_time_bars | 5.4274 |
| exposure | 0.1505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
