# EMA Hourly Continuation — ERG/USDT P12_55

**Symbol:** ERG/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1094 |
| net_profit_factor | 0.3671 |
| net_win_rate | 0.3821 |
| gross_profit_factor | 0.6506 |
| gross_win_rate | 0.4004 |
| sharpe_ratio | -9.9111 |
| sortino_ratio | -4.6274 |
| max_drawdown | 0.9970 |
| cagr | -0.8998 |
| net_avg_win | 13.8358 |
| net_avg_loss | -23.3023 |
| avg_hold_time_bars | 7.0274 |
| exposure | 0.3495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
