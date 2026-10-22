# EMA Hourly Continuation — ZK/USDT P89_144

**Symbol:** ZK/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.5189 |
| net_win_rate | 0.4426 |
| gross_profit_factor | 0.8214 |
| gross_win_rate | 0.4530 |
| sharpe_ratio | -4.5882 |
| sortino_ratio | -1.4641 |
| max_drawdown | 0.8126 |
| cagr | -0.5061 |
| net_avg_win | 41.1131 |
| net_avg_loss | -62.9151 |
| avg_hold_time_bars | 6.2171 |
| exposure | 0.1452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
