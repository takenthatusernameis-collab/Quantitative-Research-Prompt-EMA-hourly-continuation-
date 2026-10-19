# EMA Hourly Continuation — TRX/USDT P89_200

**Symbol:** TRX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.2270 |
| net_win_rate | 0.3777 |
| gross_profit_factor | 0.7666 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -7.4349 |
| sortino_ratio | -2.0501 |
| max_drawdown | 0.9403 |
| cagr | -0.6726 |
| net_avg_win | 19.8472 |
| net_avg_loss | -53.0713 |
| avg_hold_time_bars | 9.6902 |
| exposure | 0.1621 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
