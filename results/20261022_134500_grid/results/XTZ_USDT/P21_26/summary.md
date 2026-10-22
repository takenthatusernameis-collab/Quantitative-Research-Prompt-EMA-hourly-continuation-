# EMA Hourly Continuation — XTZ/USDT P21_26

**Symbol:** XTZ/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1257 |
| net_profit_factor | 0.1999 |
| net_win_rate | 0.3445 |
| gross_profit_factor | 0.8171 |
| gross_win_rate | 0.4336 |
| sharpe_ratio | -15.8337 |
| sortino_ratio | -8.2654 |
| max_drawdown | 1.0000 |
| cagr | -0.9892 |
| net_avg_win | 5.7708 |
| net_avg_loss | -15.1683 |
| avg_hold_time_bars | 1.9825 |
| exposure | 0.1133 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
