# EMA Hourly Continuation — INJ/USDT P50_55

**Symbol:** INJ/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 760 |
| net_profit_factor | 0.2089 |
| net_win_rate | 0.3526 |
| gross_profit_factor | 0.5660 |
| gross_win_rate | 0.3974 |
| sharpe_ratio | -11.4816 |
| sortino_ratio | -4.6034 |
| max_drawdown | 0.9981 |
| cagr | -0.9175 |
| net_avg_win | 9.8326 |
| net_avg_loss | -25.6425 |
| avg_hold_time_bars | 1.7671 |
| exposure | 0.0610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
