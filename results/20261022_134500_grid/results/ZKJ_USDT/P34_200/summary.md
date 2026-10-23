# EMA Hourly Continuation — ZKJ/USDT P34_200

**Symbol:** ZKJ/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 193 |
| net_profit_factor | 0.2031 |
| net_win_rate | 0.3264 |
| gross_profit_factor | 0.5813 |
| gross_win_rate | 0.3990 |
| sharpe_ratio | -5.6783 |
| sortino_ratio | -1.1361 |
| max_drawdown | 0.7812 |
| cagr | -0.4457 |
| net_avg_win | 31.2554 |
| net_avg_loss | -74.5908 |
| avg_hold_time_bars | 96.6010 |
| exposure | 0.8475 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
