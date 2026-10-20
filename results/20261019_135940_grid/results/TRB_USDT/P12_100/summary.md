# EMA Hourly Continuation — TRB/USDT P12_100

**Symbol:** TRB/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.5263 |
| net_win_rate | 0.4361 |
| gross_profit_factor | 0.7934 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -5.2965 |
| sortino_ratio | -1.9700 |
| max_drawdown | 0.9098 |
| cagr | -0.6100 |
| net_avg_win | 32.8288 |
| net_avg_loss | -48.2330 |
| avg_hold_time_bars | 17.6761 |
| exposure | 0.5631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
