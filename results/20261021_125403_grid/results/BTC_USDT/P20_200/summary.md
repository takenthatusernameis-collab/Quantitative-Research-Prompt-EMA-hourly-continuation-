# EMA Hourly Continuation — BTC/USDT P20_200

**Symbol:** BTC/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.7579 |
| net_win_rate | 0.5205 |
| gross_profit_factor | 1.0971 |
| gross_win_rate | 0.5237 |
| sharpe_ratio | -1.4388 |
| sortino_ratio | -0.3435 |
| max_drawdown | 0.3653 |
| cagr | -0.1473 |
| net_avg_win | 69.3159 |
| net_avg_loss | -99.2792 |
| avg_hold_time_bars | 49.9022 |
| exposure | 0.6328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
