# EMA Hourly Continuation — BSV/USDT P21_200

**Symbol:** BSV/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.5440 |
| net_win_rate | 0.4402 |
| gross_profit_factor | 0.8273 |
| gross_win_rate | 0.4522 |
| sharpe_ratio | -3.7762 |
| sortino_ratio | -1.0755 |
| max_drawdown | 0.7291 |
| cagr | -0.4024 |
| net_avg_win | 47.0324 |
| net_avg_loss | -67.9891 |
| avg_hold_time_bars | 33.6531 |
| exposure | 0.6394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
