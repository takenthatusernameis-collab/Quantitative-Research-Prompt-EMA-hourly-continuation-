# EMA Hourly Continuation — XTZ/USDT P8_12

**Symbol:** XTZ/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1852 |
| net_profit_factor | 0.1586 |
| net_win_rate | 0.3310 |
| gross_profit_factor | 0.7632 |
| gross_win_rate | 0.4239 |
| sharpe_ratio | -19.7676 |
| sortino_ratio | -12.5485 |
| max_drawdown | 1.0000 |
| cagr | -0.9988 |
| net_avg_win | 3.0759 |
| net_avg_loss | -9.5928 |
| avg_hold_time_bars | 1.9816 |
| exposure | 0.1668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
