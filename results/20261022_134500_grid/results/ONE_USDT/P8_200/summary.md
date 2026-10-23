# EMA Hourly Continuation — ONE/USDT P8_200

**Symbol:** ONE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.7644 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 1.0350 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -1.6432 |
| sortino_ratio | -0.4227 |
| max_drawdown | 0.4470 |
| cagr | -0.1840 |
| net_avg_win | 77.6804 |
| net_avg_loss | -101.0159 |
| avg_hold_time_bars | 53.8060 |
| exposure | 0.8193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
