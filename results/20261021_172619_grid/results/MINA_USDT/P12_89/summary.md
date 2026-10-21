# EMA Hourly Continuation — MINA/USDT P12_89

**Symbol:** MINA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.8694 |
| net_win_rate | 0.5226 |
| gross_profit_factor | 1.0854 |
| gross_win_rate | 0.5226 |
| sharpe_ratio | -0.9692 |
| sortino_ratio | -0.3212 |
| max_drawdown | 0.4139 |
| cagr | -0.1406 |
| net_avg_win | 76.0663 |
| net_avg_loss | -95.7939 |
| avg_hold_time_bars | 23.1302 |
| exposure | 0.5572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
