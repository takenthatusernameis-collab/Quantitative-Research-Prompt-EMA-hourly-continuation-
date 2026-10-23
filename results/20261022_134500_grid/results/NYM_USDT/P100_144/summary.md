# EMA Hourly Continuation — NYM/USDT P100_144

**Symbol:** NYM/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.1904 |
| net_win_rate | 0.3151 |
| gross_profit_factor | 0.5338 |
| gross_win_rate | 0.3424 |
| sharpe_ratio | -9.9562 |
| sortino_ratio | -3.2017 |
| max_drawdown | 0.9873 |
| cagr | -0.8244 |
| net_avg_win | 15.4838 |
| net_avg_loss | -37.4106 |
| avg_hold_time_bars | 5.6429 |
| exposure | 0.1221 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
