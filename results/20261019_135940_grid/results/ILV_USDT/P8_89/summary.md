# EMA Hourly Continuation — ILV/USDT P8_89

**Symbol:** ILV/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 713 |
| net_profit_factor | 0.6589 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9479 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -3.7498 |
| sortino_ratio | -1.4130 |
| max_drawdown | 0.8207 |
| cagr | -0.4878 |
| net_avg_win | 46.3616 |
| net_avg_loss | -63.7792 |
| avg_hold_time_bars | 19.2384 |
| exposure | 0.6235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
