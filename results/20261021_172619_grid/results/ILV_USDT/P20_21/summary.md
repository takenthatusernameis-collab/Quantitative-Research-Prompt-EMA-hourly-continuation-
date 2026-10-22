# EMA Hourly Continuation — ILV/USDT P20_21

**Symbol:** ILV/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 170 |
| net_profit_factor | 0.6227 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9289 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -1.8330 |
| sortino_ratio | -0.3430 |
| max_drawdown | 0.3499 |
| cagr | -0.1452 |
| net_avg_win | 64.7386 |
| net_avg_loss | -99.1916 |
| avg_hold_time_bars | 5.6941 |
| exposure | 0.0440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
