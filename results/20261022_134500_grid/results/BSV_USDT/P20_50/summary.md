# EMA Hourly Continuation — BSV/USDT P20_50

**Symbol:** BSV/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1110 |
| net_profit_factor | 0.3612 |
| net_win_rate | 0.4135 |
| gross_profit_factor | 0.8054 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -9.9458 |
| sortino_ratio | -4.6624 |
| max_drawdown | 0.9975 |
| cagr | -0.9067 |
| net_avg_win | 12.2888 |
| net_avg_loss | -23.9857 |
| avg_hold_time_bars | 4.5126 |
| exposure | 0.2277 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
