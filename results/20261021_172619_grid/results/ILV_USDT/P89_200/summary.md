# EMA Hourly Continuation — ILV/USDT P89_200

**Symbol:** ILV/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.8558 |
| net_win_rate | 0.5204 |
| gross_profit_factor | 1.0771 |
| gross_win_rate | 0.5204 |
| sharpe_ratio | -0.7460 |
| sortino_ratio | -0.1762 |
| max_drawdown | 0.1913 |
| cagr | -0.0795 |
| net_avg_win | 79.6481 |
| net_avg_loss | -101.0076 |
| avg_hold_time_bars | 17.6208 |
| exposure | 0.2155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
