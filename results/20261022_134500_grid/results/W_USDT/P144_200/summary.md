# EMA Hourly Continuation — W/USDT P144_200

**Symbol:** W/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.5452 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9354 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -3.5419 |
| sortino_ratio | -0.9890 |
| max_drawdown | 0.7175 |
| cagr | -0.3805 |
| net_avg_win | 44.8529 |
| net_avg_loss | -75.7811 |
| avg_hold_time_bars | 4.3103 |
| exposure | 0.0764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
