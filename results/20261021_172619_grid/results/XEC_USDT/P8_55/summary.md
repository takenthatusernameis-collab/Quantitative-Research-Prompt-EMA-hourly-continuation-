# EMA Hourly Continuation — XEC/USDT P8_55

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 731 |
| net_profit_factor | 0.7313 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 0.9887 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -2.7932 |
| sortino_ratio | -1.0789 |
| max_drawdown | 0.7297 |
| cagr | -0.3905 |
| net_avg_win | 53.6248 |
| net_avg_loss | -71.9343 |
| avg_hold_time_bars | 14.6922 |
| exposure | 0.4860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
