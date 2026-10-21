# EMA Hourly Continuation — XNO/USDT P8_89

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.6903 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 0.8478 |
| gross_win_rate | 0.4514 |
| sharpe_ratio | -3.1438 |
| sortino_ratio | -1.0984 |
| max_drawdown | 0.7311 |
| cagr | -0.3970 |
| net_avg_win | 58.4990 |
| net_avg_loss | -69.7341 |
| avg_hold_time_bars | 20.1862 |
| exposure | 0.5570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
