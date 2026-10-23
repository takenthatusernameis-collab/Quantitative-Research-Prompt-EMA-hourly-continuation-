# EMA Hourly Continuation — ERG/USDT P21_26

**Symbol:** ERG/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1205 |
| net_profit_factor | 0.1224 |
| net_win_rate | 0.2515 |
| gross_profit_factor | 0.3737 |
| gross_win_rate | 0.2996 |
| sharpe_ratio | -18.4694 |
| sortino_ratio | -9.6939 |
| max_drawdown | 1.0000 |
| cagr | -0.9947 |
| net_avg_win | 4.6042 |
| net_avg_loss | -12.6331 |
| avg_hold_time_bars | 2.1303 |
| exposure | 0.1167 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
