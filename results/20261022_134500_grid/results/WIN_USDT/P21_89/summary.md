# EMA Hourly Continuation — WIN/USDT P21_89

**Symbol:** WIN/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.4473 |
| net_win_rate | 0.4354 |
| gross_profit_factor | 0.8106 |
| gross_win_rate | 0.4523 |
| sharpe_ratio | -6.4555 |
| sortino_ratio | -2.3264 |
| max_drawdown | 0.9461 |
| cagr | -0.6852 |
| net_avg_win | 27.0288 |
| net_avg_loss | -46.5955 |
| avg_hold_time_bars | 13.2185 |
| exposure | 0.3905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
