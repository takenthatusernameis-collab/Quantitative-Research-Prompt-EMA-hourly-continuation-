# EMA Hourly Continuation — QNT/USDT P20_200

**Symbol:** QNT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.7159 |
| net_win_rate | 0.4968 |
| gross_profit_factor | 0.9943 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -2.3090 |
| sortino_ratio | -0.7144 |
| max_drawdown | 0.5984 |
| cagr | -0.2811 |
| net_avg_win | 60.6730 |
| net_avg_loss | -83.6772 |
| avg_hold_time_bars | 28.4416 |
| exposure | 0.6089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
