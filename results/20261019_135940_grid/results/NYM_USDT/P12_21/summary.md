# EMA Hourly Continuation — NYM/USDT P12_21

**Symbol:** NYM/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1351 |
| net_profit_factor | 0.1408 |
| net_win_rate | 0.2642 |
| gross_profit_factor | 0.5238 |
| gross_win_rate | 0.3375 |
| sharpe_ratio | -20.0455 |
| sortino_ratio | -11.2545 |
| max_drawdown | 1.0000 |
| cagr | -0.9983 |
| net_avg_win | 4.5915 |
| net_avg_loss | -11.7094 |
| avg_hold_time_bars | 3.7091 |
| exposure | 0.2278 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
