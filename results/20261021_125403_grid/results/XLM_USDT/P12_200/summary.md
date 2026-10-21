# EMA Hourly Continuation — XLM/USDT P12_200

**Symbol:** XLM/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.8833 |
| net_win_rate | 0.5258 |
| gross_profit_factor | 1.1039 |
| gross_win_rate | 0.5258 |
| sharpe_ratio | -0.6173 |
| sortino_ratio | -0.1565 |
| max_drawdown | 0.2015 |
| cagr | -0.0721 |
| net_avg_win | 79.5270 |
| net_avg_loss | -99.8376 |
| avg_hold_time_bars | 50.5000 |
| exposure | 0.7116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
