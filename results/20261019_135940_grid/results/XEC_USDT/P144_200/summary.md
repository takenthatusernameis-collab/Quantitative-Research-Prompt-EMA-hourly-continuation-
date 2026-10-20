# EMA Hourly Continuation — XEC/USDT P144_200

**Symbol:** XEC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.4103 |
| net_win_rate | 0.4431 |
| gross_profit_factor | 0.9020 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -5.5900 |
| sortino_ratio | -1.6347 |
| max_drawdown | 0.8715 |
| cagr | -0.5529 |
| net_avg_win | 32.3175 |
| net_avg_loss | -62.6832 |
| avg_hold_time_bars | 5.0142 |
| exposure | 0.0958 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
