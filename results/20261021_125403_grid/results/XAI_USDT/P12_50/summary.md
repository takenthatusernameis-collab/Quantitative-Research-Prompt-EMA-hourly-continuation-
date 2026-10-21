# EMA Hourly Continuation — XAI/USDT P12_50

**Symbol:** XAI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.7440 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 0.9224 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -3.0118 |
| sortino_ratio | -1.1427 |
| max_drawdown | 0.7535 |
| cagr | -0.4093 |
| net_avg_win | 63.8193 |
| net_avg_loss | -75.9944 |
| avg_hold_time_bars | 10.3783 |
| exposure | 0.3354 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
