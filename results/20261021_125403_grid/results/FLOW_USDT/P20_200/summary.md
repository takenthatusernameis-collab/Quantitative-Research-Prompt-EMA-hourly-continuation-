# EMA Hourly Continuation — FLOW/USDT P20_200

**Symbol:** FLOW/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.7466 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.8883 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -1.5866 |
| sortino_ratio | -0.3746 |
| max_drawdown | 0.3622 |
| cagr | -0.1595 |
| net_avg_win | 80.1305 |
| net_avg_loss | -94.9196 |
| avg_hold_time_bars | 52.1805 |
| exposure | 0.6570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
