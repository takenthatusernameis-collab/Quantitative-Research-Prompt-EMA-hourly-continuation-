# EMA Hourly Continuation — BTC/USDT P89_200

**Symbol:** BTC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.4872 |
| net_win_rate | 0.4879 |
| gross_profit_factor | 1.1565 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -4.4864 |
| sortino_ratio | -1.1979 |
| max_drawdown | 0.8352 |
| cagr | -0.4611 |
| net_avg_win | 38.9762 |
| net_avg_loss | -76.2250 |
| avg_hold_time_bars | 11.0000 |
| exposure | 0.1822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
